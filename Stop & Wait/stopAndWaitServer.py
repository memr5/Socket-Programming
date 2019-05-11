import socket
import select

s = socket.socket()
s.bind(('', 12346))

s.listen(1)

connection, addr = s.accept()

number = 1

while True:

    msg = "Packet " + str(number)

    connection.send(msg.encode('utf-8'))
    ack = False

    while not ack:

        ready = select.select([connection], [], [], 5)

        if ready[0]:
            msg = connection.recv(1024)
            print(msg.decode('utf-8'))
            ack = True
            number += 1
        else:
            connection.send(msg.encode('utf-8'))

    if msg.decode('utf-8') == 'bye':
        break
s.close()
