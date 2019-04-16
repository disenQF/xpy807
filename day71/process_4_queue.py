"""
基于Queue队列实现进程间通信
Queue对象常用的方法：
put(value, timeout) 存放数据
value = get(timeout) 读取数据
empty()  是否为空
qsize()    当前队列的大小
"""

from multiprocessing import Process
from multiprocessing import Queue

import os
import time
import random


def start_requests(queue: Queue):
    # 模拟某一网页的入口url, 下载数据
    urls = ['http://www.baidu.com/s=%s&t=%s' %(os.getpid(), time.time())
            for _ in range(100000) if _ % 1000 == 0]

    for url in urls:
        data = random.choice(['a', 'b', 'c', 'd', 'e', 'f'])
        # 向queue中存放数据
        queue.put((url, data))
        time.sleep(0.3)


def parse(queue: Queue):
    # 从queue中读取响应的数据，并进行解析
    try:
        while True:
            # 读取数据超时情况下，会抛出异常
            url, data = queue.get(timeout=5)
            print(os.getpid(), '开始解析', (url, data))
            time.sleep(0.4)
    except:
        print(os.getpid(), '任务完成')


if __name__ == '__main__':
    # 创建Queue对象
    queue = Queue(maxsize=100)

    # 创建两个进程(下载任务)
    downloads = [Process(target=start_requests, args=(queue, ))
                 for _ in range(2)]

    # 创建三个解析进程
    parses = [Process(target=parse, args=(queue,))
              for _ in range(3)]

    for process in downloads+parses:
        process.start()

    for process in downloads+parses:
        process.join()

    print('---over--')