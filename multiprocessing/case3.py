import multiprocessing
import time
def square_list(mylist, q):
    p = multiprocessing.current_process()
    print(f'{p.name}: add square in queue')
    for num in mylist:
        q.put(num * num)

def print_queue(q):
    p = multiprocessing.current_process()
    print(f"{p.name} : Queue elements")
    while not q.empty():
        time.sleep(5)
        print('print_queue',q.get())
    print(f"{p.name}: Queue is now empty!")

def sender(conn, msgs):
    p = multiprocessing.current_process()
    for msg in msgs:
        conn.send(msg)
        print(f"{p.name}: Sent the message: {msg}")
    conn.close()

def receiver(conn):
    p = multiprocessing.current_process()
    while True:
        msg = conn.recv()
        if msg == "END":
            print(f"{p.name}: {msg} found now break")
            break
        print(f"{p.name}: Received the message: {msg}")

mylist = [1,2,3,4]
q = multiprocessing.Queue()

p1 = multiprocessing.Process(target=square_list, args=(mylist, q))
p2 = multiprocessing.Process(target=print_queue, args=(q,))

p1.start()
p2.start()
p1.join()
p2.join()
