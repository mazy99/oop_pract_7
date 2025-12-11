#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from threading import Thread
from time import sleep, time


def func() -> None:
    for i in range(5):
        print(f"from child thread: {i}")
        sleep(0.5)


start_time: float = time()
print("\nБез использования join()\n")
th: Thread = Thread(target=func)
th.start()


for i in range(5):
    print(f"from main thread {i}")
    sleep(1)

end_time: float = time()
execution_time: float = end_time - start_time
print(f"Время выполнения функции без ожидания завершения потока: {execution_time}\n")

start_time_2: float = time()
print("С использованием join()\n")
th1: Thread = Thread(target=func)
th1.start()
th2: Thread = Thread(target=func)
th2.start()

for i in range(5):
    print(f"from main thread {i}")
    sleep(1)

th1.join()
th2.join()

end_time_2: float = time()
execution_time_2: float = end_time_2 - start_time_2
print(f"Время выполнения функции c ожиданием завершения потока: {execution_time_2}")
