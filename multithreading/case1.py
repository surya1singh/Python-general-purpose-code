from threading import Thread, Lock, active_count, current_thread, Timer, enumerate
import time

def do_something(a,b):
    print(a,b,current_thread())
    time.sleep(b)
    print(a,b,current_thread())
    time.sleep(b)
    print(a,b,current_thread())

def first_threads():
    first = Thread(target=do_something, args=("This is print statement is with input :",1))
    second = Thread(target=do_something, args=("This is print statement is with input :",2))
    third = Thread(target=do_something, args=("This is print statement is with input :",3))
    print(first.getName()) # prints name of the thread
    first.start()
    second.start()
    third.start()

first_threads() # create three threads
