# -*- coding: utf-8 -*-
# !/usr/bin/env python

import socket
import select
import sys

ip = input("IP: ")
port = int(input("Port: "))
name = input("Name: ")
RECV_BUFFER = 100
clients = []

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client_socket.connect((ip, port))
except:
    print("Error connexion")
    sys.exit()
clients = [sys.stdin, client_socket]
print("This client is connected to a server")

while True:
    read_sockets, write_sockets, error_sockets = select.select(clients, [], [])
    for sock in read_sockets:
        if sock == client_socket:
            message = sock.recv(RECV_BUFFER)
            if not message:
                print("The server has stopped.")
                sys.exit()
            else:
                print(message.decode())
        else:
            message_envoye = name + ": " + str(sys.stdin.readline())
            message_envoye = message_envoye.encode()
            client_socket.send(message_envoye)






