import multiprocessing
import os
import time
import datetime

def square(n):
    print(f"Worker process id for {n}: {os.getpid()}", datetime.datetime.now())
    if n in (1,4,6):
        time.sleep(12)
    time.sleep(5)
    return (n*n)


mylist = [1,2,3,4,5,6,7,8,9]


p = multiprocessing.Pool() # default is cpu_count()
result = p.map(square, mylist)
print(result)
