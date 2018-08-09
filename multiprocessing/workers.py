from log import Log_me
import multiprocessing
import sys
import time

def worker():
    p = multiprocessing.current_process()
    logger = Log_me(log_file=f'multiprocessing_{p.name}.log', log_dir='./logs/', name=p.name)
    logger.info(f'{p.name} started')
    time.sleep(10)
    logger.info(f'{p.name} ended')
    time.sleep(30)
    logger.info(f'{p.name} this line will be printed even after main program ends')

def exit_error():
    p = multiprocessing.current_process()
    logger = Log_me(log_file=f'multiprocessing_{p.name}.log', log_dir='./logs/', name=p.name)
    logger.info(f'{p.name} started')
    time.sleep(9)
    sys.exit(1)

def return_value():
    try:
        p = multiprocessing.current_process()
        logger = Log_me(log_file=f'multiprocessing_{p.name}.log', log_dir='./logs/', name=p.name)
        logger.info(f'{p.name} started')
        time.sleep(8)
        logger.info(f'{p.name} is deamon {p.deamon}')
        return 1
    except:
        logger.error(f'{p.name} faced some error')
    finally:
        logger.info(f'{p.name} ended')


def raises():
    p = multiprocessing.current_process()
    logger = Log_me(log_file=f'multiprocessing_{p.name}.log', log_dir='./logs/', name=p.name)
    logger.info(f'{p.name} started')
    logger.info(f'{p.name} raising Runtime Exception')
    raise RuntimeError()

def terminated():
    p = multiprocessing.current_process()
    logger = Log_me(log_file=f'multiprocessing_{p.name}.log', log_dir='./logs/', name=p.name)
    logger.info(f'{p.name} started')
    logger.info(f'{p.name} will be killed')
    time.sleep(15)
