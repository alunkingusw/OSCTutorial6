#!/usr/bin/python
from socket import *
myHost = ""
myPort = 2000
# Create a socket
s = socket(AF_INET, SOCK_STREAM)
# Bind the socket to the server port number
s.bind((myHost, myPort))

# Allow 5 pending connections
s.listen(5)

# Loop to continuously accept incoming connections
while True:
    # Wait for the next client to connect
    connection, address = s.accept()
    
    # Continuously receive and process data from the client
    data = connection.recv(1024)
    
    # Send the HTML response to the client
    response = """HTTP/1.0 200 OK
Content-Type: text/html

<html><body><h1>Hello World!</h1></body></html>
"""
    connection.send(response.encode('utf-8'))
        
        # Receive the next chunk of data
        #data = connection.recv(1024)
    
    # Close the connection
    connection.close()
