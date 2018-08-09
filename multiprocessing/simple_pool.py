import multiprocessing
import os
import time

def square(n):
    print(f"Worker process id for {n}: {os.getpid()}")
    time.sleep(2)
    return (n*n)

if __name__ == "__main__":
    mylist = [1,2,3,4,5,6,7,8,9]

    p = multiprocessing.Pool(6) # will create max 6 process
    result = p.map(square, mylist)
    print(result)


    p = multiprocessing.Pool() # default is cpu_count()
    result = p.map(square, mylist)
    print(result)
