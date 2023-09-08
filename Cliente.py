import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(('127.0.0.1', 12345))

while True:
    message = input("Escribe un mensaje: ")
    clientSocket.sendall(message.encode())
    response = clientSocket.recv(1024).decode()
    print("Respuesta del servidor:", response)

clientSocket.close()

