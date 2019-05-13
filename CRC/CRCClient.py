import socket
import sys


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


s = socket.socket()
s.connect(('192.168.1.103', 12345))

message = s.recv(1024).decode('utf-8')
print("Received : " + message)

generator_polynomial_bits = s.recv(1024).decode('utf-8')
print("Generator bits : " + generator_polynomial_bits)

reminder = get_reminder(generator_polynomial_bits, message)
print("Reminder : " + reminder)

if int(reminder, 2) == 0:
    s.send("ACK".encode('utf-8'))
    print("Message received without any error")
else:
    s.send("NACK".encode('utf-8'))
    print("Error in message received")

s.close()
sys.exit()
