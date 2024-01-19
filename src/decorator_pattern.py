import random
import time


def retry_decorator(func, max_retries=10, delay=1):
    def wrapper(*args, **kwargs):
        attempts = 0
        while attempts <= max_retries:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Error: {e}. Retrying in {delay} seconds.")
                time.sleep(delay)
                attempts += 1
        raise RuntimeError(f"Max retries ({max_retries}) reached. Function failed.")

    return wrapper


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        state_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {round(end_time - state_time, 2)} time to complete execution!!")
        return result

    return wrapper


@timing_decorator
@retry_decorator
def unstable_function():
    if random.randint(0, 1):
        raise ValueError('Random Failure!')
    else:
        return "success"


print(unstable_function())

# Error: Random Failure!. Retrying in 1 seconds.
# Error: Random Failure!. Retrying in 1 seconds.
# Error: Random Failure!. Retrying in 1 seconds.
# Error: Random Failure!. Retrying in 1 seconds.
# Error: Random Failure!. Retrying in 1 seconds.
# Error: Random Failure!. Retrying in 1 seconds.
# wrapper took 6.07 time to complete execution!!
# success
