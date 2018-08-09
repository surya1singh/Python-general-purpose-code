from threading import Thread, Lock
import time

firstLock = Lock()
secondLock = Lock()

def first_method():
    print(1)
    firstLock.acquire()
    time.sleep(1)
    secondLock.acquire()
    print("this should never print")

def second_method():
    print(2)
    secondLock.acquire()
    time.sleep(1)
    firstLock.acquire()
    print("this should never print too")

Thread(target=first_method).start()
Thread(target=second_method).start()
