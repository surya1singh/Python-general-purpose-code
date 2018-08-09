import multiprocessing
import time


def wait_for_event(e):
    p = multiprocessing.current_process()
    print(f'{p.name} : wait_for_event: starting')
    e.wait() # wait untill event is not set
    print(f'{p.name} : wait_for_event: e.is_set()->', e.is_set())


def wait_for_event_timeout(e, t):
    p = multiprocessing.current_process()
    print(f'{p.name} : wait_for_event_timeout: starting')
    e.wait(t) # wait for t seconds while event is not set
    print(f'{p.name} : wait_for_event_timeout: e.is_set()->', e.is_set())


if __name__ == '__main__':
    e = multiprocessing.Event()
    w1 = multiprocessing.Process(target=wait_for_event, args=(e,))
    w1.start()

    w2 = multiprocessing.Process(target=wait_for_event_timeout, args=(e, 2))
    w2.start()

    w3 = multiprocessing.Process(target=wait_for_event_timeout, args=(e, 20))
    w3.start()


    print('main: waiting before calling Event.set()')
    time.sleep(3)
    e.set()
    print('main: event is set')
