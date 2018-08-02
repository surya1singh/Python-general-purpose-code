from log import Log_me
from threading import Thread
import time

logger = Log_me(log_file='test_logging.log', log_dir='.')

def basicUse():
    logger.debug('This is debug info')
    time.sleep(0.1)
    logger.info('This is info info')
    time.sleep(0.1)
    logger.warn('This is warning info')
    time.sleep(0.1)
    logger.error('This is error info')
    time.sleep(0.1)
    logger.critical('This is critical info')


def multithreadUse():
    t1 = Thread(target=basicUse)
    t2 = Thread(target=basicUse)

    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()

    t1.join()
    t2.join()


if __name__ == '__main__':
    basicUse()
    multithreadUse()
