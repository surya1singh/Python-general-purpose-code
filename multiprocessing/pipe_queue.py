import multiprocessing

def square_list(mylist, q):
    p = multiprocessing.current_process()
    print(f'{p.name}: add square in queue')
    for num in mylist:
        q.put(num * num)

def print_queue(q):
    p = multiprocessing.current_process()
    print(f"{p.name} : Queue elements")
    while not q.empty():
        print(q.get())
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


if __name__ == "__main__":
    mylist = [1,2,3,4]
    q = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=square_list, args=(mylist, q))
    p2 = multiprocessing.Process(target=print_queue, args=(q,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()


    msgs = ["hello", "hey", "hru?", "END"]
    parent_conn, child_conn = multiprocessing.Pipe()

    p3 = multiprocessing.Process(target=sender, args=(parent_conn,msgs))
    p4 = multiprocessing.Process(target=receiver, args=(child_conn,))

    p3.start()
    p4.start()
    p3.join()
    p4.join()
