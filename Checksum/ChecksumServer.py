import socket
import sys


def ones_complement(n):
    one = ""
    for c in n:
        if c == "0":
            one += "1"
        else:
            one += "0"
    return one


server = socket.socket()
server.bind(('192.168.50.234', 12345))
server.listen(1)
checksumSize = 16

while True:

    connection, addr = server.accept()

    msg = input("Enter message : ")

    # padding of extra zeros to make message length : multiple of Checksumsize
    if len(msg) % checksumSize != 0:
        msg += "0" * (checksumSize - len(msg) % checksumSize)
        print("After padding : " + msg)

    # for calculating checksum
    checksum = 0
    j = 0
    for i in range(checksumSize, len(msg)+1, checksumSize):
        checksum += int(msg[j:i], 2)
        # print(msg[j:i] + " " + str(checksum))
        j += checksumSize

    # if checksum length is more than ChecksumSize
    # then it will convert checksum length to ChecksumSize
    checksumB = str("{0:b}".format(checksum))
    # print(checksumB)
    if len(checksumB) > checksumSize:
        # print("Checksum 1 : " + checksumB)
        e = len(checksumB) - checksumSize
        checksum = int(checksumB[0:e], 2) + int(checksumB[e:], 2)
        # print("Checksum 2 : " + str("{0:b}".format(checksum)))

    checksumB = str("{0:b}".format(checksum))
    if len(checksumB) < checksumSize:
        checksumB = "0" * (checksumSize - len(checksumB)) + checksumB
    checksumB = ones_complement(checksumB)

    # 1's complement of checksum
    # checksum = ones_complement(checksum)

    print("Binary Checksum : " + checksumB)
    print("Checksum : " + str(int(checksumB, 2)))

    connection.send((msg + checksumB).encode('utf-8'))

    # sleep(1)
    # connection.send(str(checksum).encode('utf-8'))

    ack = connection.recv(1024)

    if ack.decode('utf-8') == "ACK":
        print("Message successfully received by client")
        break
    else:
        print("Error")
server.close()
sys.exit()
