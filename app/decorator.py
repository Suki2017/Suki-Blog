__author__ = 'Suki'
import time,functools

def log(text):
    def wrapper(func):
        functools.wraps(func)
        def begin():
            print('begin call %s'%time.clock())
            func()
            print('end call %s'%time.clock())
        return begin
    return wrapper

@log
def now():
    print('now is:  %s'%time.clock())

now()

