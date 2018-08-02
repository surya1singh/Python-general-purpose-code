from threading import Thread, Lock, active_count, current_thread, Timer, enumerate
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
print("active thread at this point :", active_count())
print(current_thread()) # main thread
time.sleep(2)



threadLock = Lock()

class myThreadLock(Thread):
   def __init__(self):
      super(myThreadLock, self).__init__()

   def run(self):
      print("Starting" , self.getName())
      threadLock.acquire()
      time.sleep(1)
      print(current_thread()) # child thread
      threadLock.release()
      print("Exiting" , self.getName())


print("\n\nThreads are not synchronized")
# Create new threads
for i in range(6):
    threadX = myThreadLock()
    threadX.start()
print("Exiting Main Thread")
time.sleep(1)


# other methods
# threading.enumerate() #This function returns a list of all active threads. It is easy to use. Let us write a script to put it in use:

for thread in enumerate():
    print("Thread name is %s." % thread.getName())


#threading.Timer() #This function of threading module is used to create a new Thread and letting it know that it should only start after a specified time. Once it starts, it should call the specified function.

def delayed():
    print("I am printed after 3 seconds!")

thread = Timer(3, delayed)
thread.start()
