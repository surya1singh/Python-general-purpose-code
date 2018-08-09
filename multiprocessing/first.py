from log import Log_me
import multiprocessing
import time
import sys
from workers import worker, exit_error, return_value, raises, terminated

if __name__ == '__main__':
    a = 0
    logger = Log_me(log_file=f'multiprocessing.log', log_dir='./logs/', name='main')
    jobs = []
    funcs = [
        exit_error,
        worker,
        return_value,
        raises,
        terminated,
    ]
    for f in funcs:
        logger.info(f'Starting process for {f.__name__}')
        if a%2 == 0:
            j = multiprocessing.Process(target=f, name=f.__name__)
        else:
            j = multiprocessing.Process(target=f)

        if a%3 == 1 :
            j.daemon = True
        jobs.append(j)
        j.start()
        a+=1

    jobs[-1].terminate()
    jobs.pop(1)
    time.sleep(1)

    for j in jobs:
        j.join()
        logger.info(f'{j.name:>15}.exitcode = {j.exitcode}')
