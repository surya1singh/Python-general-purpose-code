import multiprocessing
import time
def square_list(mylist):
    p = multiprocessing.current_process()
    print(f'{p.name}:',mylist)
    time.sleep(1)
    mylist.append(1)
    print(f'{p.name}:',mylist)
    time.sleep(1)
    mylist.append(1)
    print(f'{p.name}:',mylist)
    time.sleep(1)
    mylist.append(1)
    print(f'{p.name}:',mylist)
    time.sleep(1)
    mylist.append(1)


def print_queue(mylist):
    p = multiprocessing.current_process()
    print(f'{p.name}:',mylist)
    time.sleep(1)
    mylist.append(2)
    print(f'{p.name}:',mylist)
    time.sleep(1)
    mylist.append(2)
    print(f'{p.name}:',mylist)
    time.sleep(1)
    mylist.append(2)
    print(f'{p.name}:',mylist)
    time.sleep(1)
    mylist.append(2)


def square_list1(mylist):
    p = multiprocessing.current_process()
    print(f'{p.name}:',mylist)
    time.sleep(1)
    mylist.put(1)
    print(f'{p.name}:',mylist)
    time.sleep(1)
    mylist.put(1)
    print(f'{p.name}:',mylist)
    time.sleep(1)
    mylist.put(1)
    print(f'{p.name}:',mylist)
    time.sleep(1)
    print(mylist)


def print_queue1(mylist):
    p = multiprocessing.current_process()
    print(f'{p.name}:',mylist)
    time.sleep(1)
    mylist.put(2)
    print(f'{p.name}:',mylist)
    time.sleep(1)
    mylist.put(2)
    print(f'{p.name}:',mylist)
    time.sleep(1)
    mylist.put(2)
    print(f'{p.name}:',mylist)
    time.sleep(1)
    print(mylist)

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

mylist = []
q = multiprocessing.Queue()

p1 = multiprocessing.Process(target=square_list, args=(mylist,))
p2 = multiprocessing.Process(target=print_queue, args=(mylist,))

p1.start()
p2.start()
p1.join()
p2.join()


p1 = multiprocessing.Process(target=square_list1, args=(q,))
p2 = multiprocessing.Process(target=print_queue1, args=(q,))

p1.start()
p2.start()
p1.join()
p2.join()



while not q.empty():
    print(q.get())
