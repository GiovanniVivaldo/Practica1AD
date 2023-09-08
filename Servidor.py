import socket
import threading

# Configura la dirección y el puerto del servidor
HOST = '127.0.0.1'
PORT = 12345

# Lista para mantener un registro de los clientes conectados
client_sockets = []
client_threads = []

# Función para manejar la conexión de un cliente
def handle_client(client_socket):
    try:
        while True:
            message = client_socket.recv(1024).decode()
            if not message:
                break

            print(f"Mensaje recibido: {message}")

            # Reenviar el mensaje a todos los clientes conectados
            for client in client_sockets:
                if client != client_socket:
                    client.send(message.encode())

    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        client_socket.close()
        client_sockets.remove(client_socket)

# Configura el socket del servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"Servidor en ejecución en {HOST}:{PORT}")

try:
    while True:
        client_socket, client_addr = server_socket.accept()
        print(f"Nueva conexión de {client_addr}")
        
        client_sockets.append(client_socket)
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_threads.append(client_thread)
        client_thread.start()

except KeyboardInterrupt:
    print("Servidor apagado.")
    for client_socket in client_sockets:
        client_socket.close()
    for client_thread in client_threads:
        client_thread.join()
finally:
    server_socket.close()

