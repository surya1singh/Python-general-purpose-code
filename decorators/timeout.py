import signal
import functools
import os
import time
import errno

# this decorator is copied from https://wiki.python.org/moin/PythonDecoratorLibrary#Function_Timeout

def timeout_decorator(seconds=60, error_message=os.strerror(errno.ETIME)):
    def decorator(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError(error_message)

        def wrapper(*args, **kwargs):
            print(kwargs)
            timeout = kwargs.get('timeout')
            if not timeout:
                timeout = seconds
            print(timeout)
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(timeout)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result
        return functools.wraps(func)(wrapper)

    return decorator


if __name__ == "__main__":

    @timeout_decorator()
    def foo(*args, **kwargs):
        print(1)
        time.sleep(10)
        print(2)
        
    foo(timeout = 5)
