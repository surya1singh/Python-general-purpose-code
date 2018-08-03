# run 25 thread with max 8 running at a time
from queue import Queue
from threading import Thread
import time

def foo():
    print("")



class myThread(Thread):
   def __init__(self):
        super(myThread, self).__init__()

   def run(self):
        print("Starting" , self.getName())
        time.sleep(1)
        print("Exiting" , self.getName())
        q.get()



q = Queue(maxsize = 8)

print(dir(q))

for i in range(25):
    while True:
        if q.full():
            time.sleep(1)
            continue
        else:
            q.put(1)
            myThread().start()
            break
