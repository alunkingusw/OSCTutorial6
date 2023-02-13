from socket import *
import sys
import time
import os
myHost = ""
myPort = 2000
# create a UDP socket
s=socket(AF_INET, SOCK_DGRAM)
# bind it to the server port number
s.bind((myHost, myPort))

while True:
    data, address = s.recvfrom(1024)
    print ("UDP server:", data, "from", address)
    if data:
        start_time = time.time()
        print ("processing request received")
        time.sleep (5)
        end_time = time.time()
        print ("processing took: ", end_time-start_time, "seconds")
        s.sendto(("echo -> " + data.decode('utf-8')).encode('utf-8'), address)
    else:
        break
