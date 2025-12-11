#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from threading import Lock, Thread
from time import sleep

lock: Lock = Lock()

stop_thread: bool = False


def infinit_worker() -> None:
    print("Start infinit_worker")
    while True:
        print("---> thread work")
        lock.acquire()

        if stop_thread is True:
            break
        lock.release()
        sleep(0.1)
    print("Stop infinit_worker()")


if __name__ == "__main__":
    th: Thread = Thread(target=infinit_worker)
    th.start()
    sleep(2)
    lock.acquire()
    stop_thread = True
    lock.release()
