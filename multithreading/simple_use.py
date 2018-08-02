from threading import Thread, Lock
import time

def first_threads():
    first = Thread(target=print, args=("This is print statement is with input :",1))
    second = Thread(target=print, args=("This is print statement is with input :",2))
    third = Thread(target=print, args=("This is print statement is with input :",3))
    print(first.getName()) # prints name of the thread
    first.start()
    second.start()
    third.start()

first_threads() # create three threads



class myThread(Thread):
   def __init__(self):
      super(myThread, self).__init__()

   def run(self):
      print("Starting" , self.getName())
      time.sleep(1)
      print("Exiting" , self.getName())


print("Threads are not synchronized")
# Create new threads
for i in range(6):
    threadX = myThread()
    threadX.start()
print("Exiting Main Thread")
time.sleep(2)



threadLock = Lock()

class myThreadLock(Thread):
   def __init__(self):
      super(myThreadLock, self).__init__()

   def run(self):
      print("Starting" , self.getName())
      threadLock.acquire()
      time.sleep(1)
      threadLock.release()
      print("Exiting" , self.getName())


print("\n\nThreads are not synchronized")
# Create new threads
for i in range(6):
    threadX = myThreadLock()
    threadX.start()
print("Exiting Main Thread")
time.sleep(1)
