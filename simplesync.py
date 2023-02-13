#!/usr/bin/env python
import sys, time
from _thread import start_new
from threading import Semaphore
sync = Semaphore(value=0)
def processA (p, count):
    global sync
    print ("processA", p, "comes to life")
    while True:
        time.sleep (5) # do some work
        sync.release() # indicate we have finished our work
def processB (p, count):
    global sync
    print ("processB", p, "comes to life")
    while True:
        print ("waiting for process A to complete its work")
        start_time = time.time()
        sync.acquire()
        end_time = time.time()
        print ("processB", p, "spent", end_time - start_time, "seconds waiting to for process A to finish")

def main ():
    start_new(processA, (1, 0))
    processB (2, 0)

main ()
