Гаврилюк Максим ІПС-31 
Варіант 7
SSL
Secure Sockets Layer (SSL) — це криптографічний протокол, що забезпечує захищену передачу даних через комп'ютерну мережу. Розроблений компанією Netscape Communications на початку 1990-х років. Використовуючи симетричне шифрування для шифрування самої інформації та асиметричне шифрування для обміну ключами. 	
Алгоритм:
1.	Клієнт надсилає запит на сервер за допомогою протоколу HTTP або HTTPS.
2.	Сервер відповідає, пропонуючи свій сертифікат, який містить публічний ключ та інформацію про сервер.
3.	Клієнт перевіряє валідність сертифіката за допомогою надійного центру сертифікації (Certificate Authority, CA).
4.	Якщо сертифікат валідний, клієнт створює симетричний ключ шифрування та використовує публічний ключ сервера для його зашифрування.
5.	Клієнт надсилає зашифрований симетричний ключ на сервер.
6.	Сервер використовує свій приватний ключ для розшифрування симетричного ключа.
7.	Клієнт і сервер мають спільний симетричний ключ для шифрування та розшифрування даних, які будуть передаватися між ними.

Signature algorithm Schnorr
Алгоритм підпису Schnorr є криптографічним протоколом для створення та перевірки цифрових підписів. Цей алгоритм був розроблений Клаусом Шнорром в 1989 році і вважається одним з найбільш ефективних та безпечних алгоритмів підпису. 
Основна ідея алгоритму Schnorr полягає в використанні дискретних логарифмів на еліптичних кривих. Алгоритм вимагає вибору великого простого числа p та еліптичної кривої E над цим полем. Згодом обирається точка P на цій кривій, яка буде використовуватись як генератор групи підпису.
Процес створення підпису Schnorr включає наступні кроки:	
1.	Генерація ключів:
•	Вибір випадкового секретного ключа d, де 1 <= d <= p-2.
•	Обчислення публічного ключа Q = d * P.
2.	Підготовка повідомлення та обчислення випадкового значення:
•	Вибір повідомлення m, яке потрібно підписати.
•	Вибір випадкового значення k, де 1 <= k <= p-1.
3.	Обчислення підпису:
•	Обчислення точки R = k * P.
•	Обчислення хеш-функції повідомлення H(m).
•	Обчислення підпису s = k + d * H(m) mod (p-1).
4.	Представлення підпису:
•	Підпис складається з пари значень (R, s), де R - координати точки R, а s - підпис.
Процес перевірки підпису Schnorr включає наступні кроки:
1.	Отримання публічного ключа Q та підпису (R, s).
2.	Обчислення хеш-функції повідомлення H(m).
3.	Перевірка підпису:
•	Обчислення точки u1 = s * P - H(m) * Q.
•	Обчислення хеш-функції u2 = H(u1 || R).
•	Підпис вірний, якщо u2 дорівнює х-координаті R.
