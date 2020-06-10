### 手动制造一个僵尸进程demon
### 我们使用日常开发中经常使用的 multiprocessing 模块来制造僵尸进程（准确的来说是制造一个长时间维持僵尸进程状态的子进程）

from multiprocessing import Process, current_process
import logging
import os
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)-15s - %(levelname)s - %(message)s'
)


def run():
    logging.info('exit child process %s', current_process().pid)
    os._exit(3)

p = Process(target=run)
p.start()
time.sleep(100)