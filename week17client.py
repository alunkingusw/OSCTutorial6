#!/usr/bin/python

import sys
from socket import *
serverHost = "localhost"
serverPort = 2000

#create a TCP socket
s = socket(AF_INET, SOCK_STREAM)

s.connect((serverHost, serverPort))
s.send("Hello There".encode('utf-8'))
data = s.recv(1024)
print(data)
s.close()
