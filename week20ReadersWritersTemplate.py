#!/usr/bin/env python
from random import randrange
from re import I
import sys, time
from _thread import start_new
from threading import Semaphore

#this is used to make sure that the print out functions normally.
mutexPrint = Semaphore(value=1)

readers_reading = 0
writers_writing = 0


def printf (format, *args):
    global mutexPrint, m
    mutexPrint.acquire()
    print (str(format) % args,)
    mutexPrint.release()

def reader (p, count):
    global readers_reading, writers_writing
    printf("reader %d started\n", p)
    while True:
        printf ("reader %d looking to read data structure", p)
        
        readers_reading += 1
        
        #read for a while
        time.sleep(randrange(1,5))

        #check if we are altering while readers are reading
        if(writers_writing > 0):
            printf("There are writers writing!! Fatal error")
            sys.exit(1)

        readers_reading -= 1

        printf ("reader %d finished reading", p)
    
        printf ("reader %d resting now. Current readers: %d, and writers:\n", p, readers_reading, writers_writing)
        time.sleep(randrange(1,5))

def writer (p, count):
    global readers_reading, writers_writing
    printf("writer %d started\n", p)
    while True:
        printf ("writer %d needs to write to data structure", p)

        #checks needed here
        writers_writing += 1

        #check if we are altering while readers are reading
        if(readers_reading > 0 or writers_writing > 1):
            printf("There are readers reading!! Fatal error")
            sys.exit(1)
        
        writers_writing -= 1

        printf ("writer %d finished writing.", p)
        printf ("writer %d resting now. Current readers: %d, and writers: %d\n", p, readers_reading, writers_writing)
        time.sleep (randrange(1,2))

def main ():
    start_new(reader, (1, 0))
    #start_new(consumer,(2,0))
    #start_new(consumer,(3,0))
    #start_new(producer,(4,0))
    writer(5,0)


main ()
