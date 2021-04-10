# 2. Print current date by using 2 threads.
# #1. Define a subclass using Thread class.
# #2. Instantiate the subclass and trigger the thread.

from threading import Thread
import datetime

class MyThread(Thread):
    def run(self) -> None:
        print(f"Thread - {self.name}. Current date is {datetime.date.today()}")
        print(f"Thread - {self.name}. Current time is {datetime.datetime.now().time()}")

my_thread_1 = MyThread()
my_thread_2 = MyThread()

my_thread_1.start()
my_thread_2.start()
