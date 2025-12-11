#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from threading import Thread
from time import sleep, time


class CustomThread(Thread):
    def __init__(self, limit: int) -> None:
        Thread.__init__(self)
        self.limit_: int = limit

    def run(self) -> None:
        for i in range(self.limit_):
            print(f"from CustomThread: {i}")
            sleep(0.5)


if __name__ == "__main__":
    start_time: float = time()

    cth = CustomThread(10)
    cth.start()
    cth.join()

    end_time: float = time()
    execution_time: float = end_time - start_time

    print(f"\nВремя выполнения: {execution_time} секунд")
