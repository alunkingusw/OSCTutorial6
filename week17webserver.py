#!/usr/bin/python
from socket import *
myHost = ""
myPort = 2001
# create a socket
s = socket(AF_INET, SOCK_STREAM)
# bind it to the server port number
s.bind((myHost, myPort))
# allow 5 pending connections
s.listen(5)
while True:
    # wait for next client to connect
    connection, address = s.accept()
    print("connection accepted")
    data = connection.recv(1024)
    print("sending data")
    reply = """HTTP-Version: HTTP/1.0 200 OK
Content-Length: 3012
Content-Type: text/html

<html>
<body><h1>Hello world!</h1></body></html>
""".encode()
    connection.send(reply)
    print("sent")
    connection.close()
