# -*- coding: utf-8 -*-
# !/usr/bin/env python

import socket
import select
import random

def broadcast(sock_, message_):
    for sock in clients:
        if sock != server_socket and sock != sock_:
            try:
                sock.send(message_)
            except:
                sock.close()
                clients.remove(sock)

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
port = random.randint(2**10+1, 2**16-1)
clients = list()
RECV_BUFFER = 100

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((ip, port))
server_socket.listen(5)
clients.append(server_socket)
print("The server is ip {}, port {}.".format(ip, str(port)))	

while True:
    read_sockets, write_sockets, error_sockets = select.select(clients, [], [])
    for sock in read_sockets:
        if sock == server_socket:
            client_socket, client_infos = server_socket.accept()
            clients.append(client_socket)
            print("New client {} connected.".format(client_infos[1]))
        else:
            try:
                message = sock.recv(RECV_BUFFER)
                if not message:
                    print("Client disconnected.")
                    sock.close()
                    clients.remove(sock)
                else:
                    broadcast(sock, message)
            except:
                sock.close()
                clients.remove(sock)
                print("Unexpected error.")
                continue



