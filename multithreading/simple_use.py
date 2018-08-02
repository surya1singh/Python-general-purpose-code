from threading import Thread
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



# Create new threads
thread1 = myThread()
thread2 = myThread()

# Start new Threads
thread1.start()
thread2.start()

print("Exiting Main Thread")
