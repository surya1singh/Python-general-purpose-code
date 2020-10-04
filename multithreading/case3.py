from threading import Thread, Lock, active_count, current_thread, Timer, enumerate
import time

for thread in enumerate():
    print("Thread name is %s." % thread.getName())


#threading.Timer() #This function of threading module is used to create a new Thread and letting it know that it should only start after a specified time. Once it starts, it should call the specified function.
def foo():
    while True:
        delayed()
        time.sleep(2)

def delayed():
    print("ping the server",thread.getName())
    print("exit the server",thread.getName())

thread1 = Thread(target=foo)


thread1.start()
print("this will print after thread1 finish")
