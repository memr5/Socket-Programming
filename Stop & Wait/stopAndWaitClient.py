import socket
import sys
import select

s = socket.socket()
s.connect(('192.168.1.148', 12346))

while True:

    input_stream = [sys.stdin, s]

    read_soc, write_soc, error_sock = select.select(input_stream, [], [])

    for soc in read_soc:
        if soc == s:
            msg = s.recv(1024).decode('utf-8')
            print(msg)
        else:
            msg = input()
            s.send(msg.encode('utf-8'))
        if msg == 'bye':
            input_stream.remove(s)
    if s not in input_stream:
        break

s.close()
