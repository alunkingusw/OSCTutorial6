#!/usr/bin/python

from socket import *
myHost = "localhost"
myPort = 2000

#create a socket
s = socket(AF_INET, SOCK_STREAM)
#bind it to the server port number
try:
    s.bind((myHost, myPort))
except socket.error as e:
    print(e)
    #allow 5 pending connections
s.listen(5)

while True:
    #wait for next client to connect
    connection, address = s.accept()
    data = connection.recv(1024)
    print(data.decode('utf-8'))
    while data:
        connection.send(data)
        data = connection.recv(1024)
        print(data.decode('utf-8'))
    connection.close()
