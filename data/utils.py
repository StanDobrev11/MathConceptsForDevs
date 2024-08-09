from time import time


def measure_execution_time(func):
    """ decorator to track time elapsed """

    def wrapper(*args):
        start_time = time()
        result = func(*args)
        end_time = time()
        timedelta = end_time - start_time
        return {'time': timedelta, 'result': result}

    return wrapper
