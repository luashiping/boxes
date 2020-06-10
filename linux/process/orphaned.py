### 什么是孤儿进程：当父进程已经退出但是子进程仍旧在运行时，这个子进程就变成了孤儿进程。 系统会把孤儿进程的父进程设置为 init 进程，将由 init 进程来管理这个孤儿进程。

from multiprocessing import Process, current_process
import logging
import os
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)-15s - %(levelname)s - %(message)s'
)


def run():
    time.sleep(30)
    logging.info('exit grandchild process %s', current_process().pid)
    os._exit(3)


def worker():
    p = Process(target=run)
    p.start()
    logging.info('exit worker process %s, grandchild is %s',
                 current_process().pid, p.pid)
    os._exit(1)


p = Process(target=worker)
p.start()
p.join()
time.sleep(100)