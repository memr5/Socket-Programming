import socket
import sys
from time import sleep


def xor(a, b):

    result = ""

    for i in range(1, len(b)):
        if a[i] == b[i]:
            result += "0"
        else:
            result += "1"
    return result


def get_reminder(divisor, divident):

    pick = len(divisor)
    temp = divident[0:pick]

    while pick < len(divident):

        if temp[0] == "1":
            temp = xor(divisor, temp) + divident[pick]

        else:
            temp = xor("0"*pick, temp) + divident[pick]

        pick += 1

    if temp[0] == "1":
        temp = xor(divisor, temp)

    else:
        temp = xor("0"*pick, temp)

    return temp


server = socket.socket()
server.bind(('', 12345))
server.listen(1)

generator_polynomial_bits = "1101"

connection, addr = server.accept()

message = input("Enter message : ")

reminder = get_reminder(generator_polynomial_bits, message + "0" * (len(generator_polynomial_bits)-1))

message = message + reminder
print("Final message : " + message + " crc in binary : " + reminder)

connection.send(message.encode('utf-8'))
sleep(2)
connection.send(generator_polynomial_bits.encode('utf-8'))

received = connection.recv(1024).decode('utf-8')

if received == "ACK":
    print("Message successfully sent")
else:
    print("Error")

server.close()
sys.exit()
