import multiprocessing
import time

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


msgs = ["hello", "hey", "hru?", "END"]
parent_conn, child_conn = multiprocessing.Pipe()

p3 = multiprocessing.Process(target=sender, args=(parent_conn,msgs))
p4 = multiprocessing.Process(target=receiver, args=(child_conn,))

p3.start()
p4.start()
p3.join()
p4.join()
