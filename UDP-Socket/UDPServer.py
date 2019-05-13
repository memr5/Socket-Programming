import socket
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('', 12345))

while True:

    message, client = server.recvfrom(1024)
    print("Received : ", message.decode('utf-8'))

    if message.decode('utf-8') == "bye":
        break

    message = input("Enter message to send : ")
    server.sendto(message.encode('utf-8'), client)

    if message == "bye":
        break

server.close()
sys.exit(0)
