import threading
from server import start_ssl_server
from client import start_ssl_client


if __name__ == "__main__":
    # Create and start the server thread
    server_thread = threading.Thread(target=start_ssl_server)
    server_thread.start()

    # Create and start the client thread
    client_thread = threading.Thread(target=start_ssl_client)
    client_thread.start()

    # Wait for both threads to finish
    server_thread.join()
    client_thread.join()
