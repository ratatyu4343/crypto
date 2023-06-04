import socket
import ssl
import datetime
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes

def create_self_signed_cert_key():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )

    subject = issuer = x509.Name([
        x509.NameAttribute(x509.NameOID.COUNTRY_NAME, u"US"),
        x509.NameAttribute(x509.NameOID.STATE_OR_PROVINCE_NAME, u"California"),
        x509.NameAttribute(x509.NameOID.LOCALITY_NAME, u"San Francisco"),
        x509.NameAttribute(x509.NameOID.ORGANIZATION_NAME, u"My Organization"),
        x509.NameAttribute(x509.NameOID.COMMON_NAME, u"localhost"),
    ])

    cert = x509.CertificateBuilder().subject_name(
        subject
    ).issuer_name(
        issuer
    ).public_key(
        private_key.public_key()
    ).serial_number(
        x509.random_serial_number()
    ).not_valid_before(
        datetime.datetime.utcnow()
    ).not_valid_after(
        datetime.datetime.utcnow() + datetime.timedelta(days=365)
    ).add_extension(
        x509.SubjectAlternativeName([x509.DNSName(u"localhost")]),
        critical=False
    ).sign(private_key, hashes.SHA256(), default_backend())

    private_key_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    cert_pem = cert.public_bytes(serialization.Encoding.PEM)

    return cert_pem, private_key_pem

def receive_data(client_ssl_socket):
    # Отримати дані від клієнта
    data = client_ssl_socket.recv(1024)
    return data

def send_data(client_ssl_socket, data):
    # Надіслати дані клієнту
    client_ssl_socket.send(data)

def create_ssl_context():
    cert_pem, private_key_pem = create_self_signed_cert_key()

    # Створення порожнього SSL контексту
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)

    # Встановлення самопідписаного сертифікату та приватного ключа
    context.load_cert_chain(certfile=cert_pem, keyfile=private_key_pem)
    
    return context

def pseudo_certificate_verification(client_ssl_socket):
    # Перевірка сертифікату
    certificate = client_ssl_socket.getpeercert()
    print("SERVER: Received Certificate:", certificate)

def pseudo_encrypt_decrypt(data):
    # Шифрування та розшифрування
    return decrypted_data

def ssl_handshake(client_socket, ssl_context):
    # Виконати SSL handshake з клієнтом
    client_ssl_socket = ssl_context.wrap_socket(client_socket, server_side=True)
    return client_ssl_socket

def ssl_communication(client_ssl_socket):
    # Виконати захищену комунікацію з клієнтом
    while True:
        data = receive_data(client_ssl_socket)
        if not data:
            break
        decrypted_data = pseudo_encrypt_decrypt(data)
        print("SERVER: Received:", data.decode())
        print("SERVER: Decrypted:", decrypted_data)
        encrypted_response = pseudo_encrypt_decrypt(decrypted_data.encode())
        send_data(client_ssl_socket, encrypted_response.encode())

def start_ssl_server():
    # Створити серверний сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 8080))
    server_socket.listen(1)

    # Очікувати підключaення клієнта
    client_socket, addr = server_socket.accept()
    print("SERVER: Connected by:", addr)

    # Створити SSL контекст
    ssl_context = create_ssl_context()

    # Виконати SSL handshake
    client_ssl_socket = ssl_handshake(client_socket, ssl_context)

    # Виконати псевдоперевірку сертифікату
    pseudo_certificate_verification(client_ssl_socket)

    # Запустити захищену комунікацію
    ssl_communication(client_ssl_socket)

    # Закрити з'єднання
    client_ssl_socket.close()
    server_socket.close()
