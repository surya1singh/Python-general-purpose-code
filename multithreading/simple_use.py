from threading import Thread
import time

first = Thread(target=print, args=("This is print statement is with input :",1))
second = Thread(target=print, args=("This is print statement is with input :",2))
third = Thread(target=print, args=("This is print statement is with input :",3))
print(first.getName())
first.start()
second.start()
third.start()
