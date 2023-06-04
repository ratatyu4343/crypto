import hashlib
import random
from sympy import mod_inverse

# Вибір великого простого числа p та еліптичної кривої E над цим полем
p = 2147483647  # Приклад простого числа p
a = -1  # Коефіцієнт a еліптичної кривої
b = 0   # Коефіцієнт b еліптичної кривої

# Генерація ключів
def generate_keys():
    # Вибір випадкового секретного ключа d, де 1 <= d <= p-2
    d = random.randint(1, p-2)
    
    # Обчислення публічного ключа Q = d * P
    Q = multiply_point(d, P)
    
    return d, Q

# Обчислення точки R = k * P
def sign(message, d, Q):
    # Вибір випадкового значення k, де 1 <= k <= p-1
    k = random.randint(1, p-1)
    
    # Обчислення точки R = k * P
    R = multiply_point(k, P)
    
    # Обчислення хеш-функції повідомлення H(m)
    h = hashlib.sha256(message.encode()).digest()
    h = int.from_bytes(h, byteorder='big')
    
    # Обчислення підпису s = k + d * H(m) mod (p-1)
    s = (k + d * h) % (p-1)
    
    return R, s

# Перевірка підпису
def verify(message, Q, signature):
    R, s = signature
    
    # Обчислення хеш-функції повідомлення H(m)
    h = hashlib.sha256(message.encode()).digest()
    h = int.from_bytes(h, byteorder='big')
    
    # Обчислення точки u1 = s * P - H(m) * Q
    u1 = add_points(multiply_point(s, P), multiply_point(h, Q))
    
    if u1 is None:
        return False
    
    # Обчислення хеш-функції u2 = H(u1 || R)
    u1_bytes = u1.x.to_bytes(32, byteorder='big') + u1.y.to_bytes(32, byteorder='big')
    u2 = hashlib.sha256(u1_bytes + R.x.to_bytes(32, byteorder='big')).digest()
    u2 = int.from_bytes(u2, byteorder='big')
    
    # Підпис вірний, якщо u2 дорівнює х-координаті R
    if u2 == R.x % p:
        return True
    else:
        return False

# Клас, що представляє точку на еліптичній кривій
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Функція для додавання двох точок на еліптичній кривій
def add_points(point1, point2):
    if point1 is None:
        return point2
    if point2 is None:
        return point1
    if point1.x == point2.x and point1.y != point2.y:
        return None
    if point1.x == point2.x:
        m = (3 * point1.x * point1.x + a) * mod_inverse(2 * point1.y, p) % p
    else:
        m = (point1.y - point2.y) * mod_inverse((point1.x - point2.x) % p, p) % p
    x = (m * m - point1.x - point2.x) % p
    y = (m * (point1.x - x) - point1.y) % p
    return Point(x, y)

# Функція для множення точки на скаляр
def multiply_point(scalar, point):
    result = None
    addend = point
    while scalar:
        if scalar & 1:
            result = add_points(result, addend)
        addend = add_points(addend, addend)
        scalar >>= 1
    return result

# Вибір точки P, яка буде використовуватись як генератор групи підпису
P = Point(2, 3)  # Приклад точки P

# Приклад використання
message = "Hello, world!"

# Генерація ключів
d, Q = generate_keys()

# Підпис повідомлення
signature = sign(message, d, Q)

# Перевірка підпису
valid = verify(message, Q, signature)

# Виведення результату перевірки
if valid:
    print("Підпис вірний.")
else:
    print("Підпис невірний.")
