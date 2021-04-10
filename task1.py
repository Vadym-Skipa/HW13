# 1. Write the method that return the number of threads currently in execution.
# Also prepare the method that will be executed with threads and run during the first method counting.

from threading import Thread, active_count
from time import sleep

counter = 0

def triple_doing_with_pause_between_doing(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        sleep(1)
        func(*args, **kwargs)
        sleep(1)
        return func(*args, **kwargs)

    return inner

@triple_doing_with_pause_between_doing
def my_function():
    global counter
    print(f"Doing something {counter}")
    counter += 1

def print_number_of_thread():
    print(f"Number of thread objects currently alive is {active_count()}")

thread1 = Thread(target=my_function)
thread2 = Thread(target=my_function)
thread3 = Thread(target=my_function)
thread4 = Thread(target=my_function)
thread5 = Thread(target=my_function)

thread1.start()
thread2.start()
thread3.start()
thread4.start()
print_number_of_thread()
thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.start()
print_number_of_thread()
thread5.join()
print_number_of_thread()