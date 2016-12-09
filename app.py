#!/usr/bin/env python

import sys
import socket

TCP_IP = ''
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

while True:
    # wait for connection
    conn, addr = s.accept()
    try:
        sys.stderr.print('Connection address:', addr, '\n')
        while 1:
            data = conn.recv(BUFFER_SIZE)
            if not data: break
            sys.stderr.print('got data:', data, '\n')
            conn.send(data)  # echo
    finally:
        sys.stderr.print('Closing connection\n')
        conn.close()
