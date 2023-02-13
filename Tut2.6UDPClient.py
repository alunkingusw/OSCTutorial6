#!/usr/bin/python
import sys, time
from socket import *
serverHost = "localhost"
serverPort = 2000
# create a UDP socket
s=socket(AF_INET, SOCK_DGRAM)

s.connect((serverHost, serverPort))
start_time = time.time()
s.send("Hello world".encode('utf-8'))
data = s.recv(1024)
end_time = time.time()
print (data.decode('utf-8'))
print ("time to send to server and get reply was", end_time - start_time, "seconds")
