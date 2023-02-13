#!/usr/bin/env python
import sys, time
from _thread import start_new
from threading import Semaphore
mutex = Semaphore(value=1)
printMutex = Semaphore(value=1)
n=0
m=0 #global variable which will be incremented and
    # decremented inside the critical region


def printf (format, *args):
    global printMutex, m
    printMutex.acquire()
    m += 1
    if m != 1:
        printf ("something has gone very wrong!\n")
        sys.exit (1)
        
        
    print (str(format) % args,)
    m -= 1
    printMutex.release()

def process (p, count):
    global mutex, n
    printf ("process %d comes to life\n", p)
    while True:
        start_time = time.time()
        printf ("process %d waiting to enter\n", p)
        mutex.acquire()
        end_time = time.time()
        printf ("process %d spent %f seconds waiting to enter the critical region\n", p, end_time-start_time)
        # critical region
        n += 1
        if n != 1:
            printf ("something has gone very wrong!\n")
            sys.exit (1)
        time.sleep (5)
        n -= 1
        mutex.release()
        printf ("process %d finished critical region\n",p)

def main ():
    for i in range (3):
        start_new(process, (i, 0))
    process (4, 0)
main ()
