import socket
import sys

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip_address = '192.168.1.107'
port = 12345

while True:

    message = input("Enter message to send : ")
    client.sendto(message.encode('utf-8'), (ip_address, port))

    if message == "bye":
        break

    message, server = client.recvfrom(1024)
    print("Received : ", message.decode('utf-8'))

    if message.decode('utf-8') == "bye":
        break

client.close()
sys.exit(0)
