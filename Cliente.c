#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

int main() {
    int clientSocket;
    struct sockaddr_in serverAddr;
    char buffer[1024];

    // Crear el socket
    clientSocket = socket(AF_INET, SOCK_STREAM, 0);

    // Configurar la dirección del servidor
    serverAddr.sin_family = AF_INET;
    serverAddr.sin_port = htons(12345);
    serverAddr.sin_addr.s_addr = inet_addr("127.0.0.1");

    // Conectar al servidor
    connect(clientSocket, (struct sockaddr*)&serverAddr, sizeof(serverAddr));

    while (1) {
        printf("Escribe un mensaje: ");
        fgets(buffer, sizeof(buffer), stdin);
        send(clientSocket, buffer, strlen(buffer), 0);

        // Leer la respuesta del servidor
        recv(clientSocket, buffer, sizeof(buffer), 0);
        printf("Respuesta del servidor: %s\n", buffer);
    }

    close(clientSocket);
    return 0;
}

