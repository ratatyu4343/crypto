import socket
import ssl

def receive_data(server_ssl_socket):
    # Отримати дані від сервера
    data = server_ssl_socket.recv(1024)
    return data

def send_data(server_ssl_socket, data):
    # Надіслати дані серверу
    server_ssl_socket.send(data)

def create_ssl_context():
    # Створити SSL контекст
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    return context

def pseudo_certificate_verification(server_ssl_socket):
    # перевірка сертифікату
    certificate = server_ssl_socket.getpeercert()
    print("CLIENT: Received Certificate:", certificate)

def pseudo_encrypt_decrypt(data):
    # шифрування та розшифрування
    return decrypted_data

def ssl_handshake(server_socket, ssl_context):
    # Виконати SSL handshake з сервером
    server_ssl_socket = ssl_context.wrap_socket(server_socket)
    return server_ssl_socket

def ssl_communication(server_ssl_socket):
    # Виконати захищену комунікацію з сервером
    while True:
        message = input("CLIENT: Enter message (or 'quit' to exit): ")
        if message.lower() == "quit":
            break
        encrypted_message = pseudo_encrypt_decrypt(message.encode())
        send_data(server_ssl_socket, encrypted_message.encode())
        response = receive_data(server_ssl_socket)
        decrypted_response = pseudo_encrypt_decrypt(response.decode())
        print("CLIENT: Received:", response.decode())
        print("CLIENT: Decrypted:", decrypted_response)

def start_ssl_client():
    # Створити сокет клієнта
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost", 8080))

    # Створити SSL контекст
    ssl_context = create_ssl_context()

    # Виконати SSL handshake
    server_ssl_socket = ssl_handshake(client_socket, ssl_context)

    # Виконати псевдоперевірку сертифікату
    pseudo_certificate_verification(server_ssl_socket)

    # Запустити захищену комунікацію
    ssl_communication(server_ssl_socket)

    # Закрити з'єднання
    server_ssl_socket.close()
    client_socket.close()
