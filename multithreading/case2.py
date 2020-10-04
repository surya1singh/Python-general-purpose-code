from threading import Thread, Lock, active_count, current_thread, Timer, enumerate
import time


threadLock = Lock()

class myThreadLock(Thread):
   def __init__(self):
      super(myThreadLock, self).__init__()

   def run(self):
      print("Starting" , self.getName())
      time.sleep(3)
      threadLock.acquire()
      time.sleep(2)
      print(current_thread()) # child thread
      threadLock.release()
      print("Exiting" , self.getName())


print("\n\nThreads are not synchronized")
# Create new threads
threadX = myThreadLock()
threadX.start()


def do_something():
    if threadLock.locked():
        print("this will only happen after lock if acquired")
    else:
        print("first acquire lock")
        time.sleep(1)
        do_something()

first = Thread(target=do_something)
first.start()

for thread in enumerate():
    print("Thread name is %s." % thread.getName())
