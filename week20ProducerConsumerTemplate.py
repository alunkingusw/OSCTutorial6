#!/usr/bin/env python
from random import randrange
from re import I
import sys, time
from _thread import start_new
from threading import Semaphore

#this is used to make sure that the print out functions normally.
mutexPrint = Semaphore(value=1)

BUFFER_LIMIT = 15

buffer=10 #integer indicating items available in buffer


def printf (format, *args):
    global mutexPrint, m
    mutexPrint.acquire()
    print (str(format) % args,)
    mutexPrint.release()

def producer (p, count):
    global buffer
    printf("producer %d started\n", p)
    while True:
        printf ("producer %d looking to produce an item", p)
        
        #checks needed here
        buffer += 1
        
        #check if we have produced too much
        if(buffer > BUFFER_LIMIT):
            printf("Buffer overflow!! Quitting")
            sys.exit(randrange(1,2))
            
        printf ("producer %d deposited an item to buffer", p)
    
        printf ("producer %d going to get more stuff. Current items in buffer: %d\n", p, buffer)
        time.sleep(1)

def consumer (p, count):
    global buffer
    printf("consumer %d started\n", p)
    while True:
        printf ("consumer %d looking to consume an item", p)

        #checks needed here
        buffer -= 1

        #check if we have consumed too much
        if(buffer < 0):
            printf("Not enough items to consume!! Quitting")
            sys.exit(1)
        
        printf ("consumer %d comsumed from the buffer. Nom nom nom.", p)
        printf ("consumer %d going to rest now. Current items in buffer: %d\n", p, buffer)
        time.sleep (randrange(1,2))

def main ():
    start_new(producer, (1, 0))
    #start_new(consumer,(2,0))
    #start_new(consumer,(3,0))
    #start_new(producer,(4,0))
    consumer(5,0)


main ()
