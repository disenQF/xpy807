"""
设计模式中的生产者与消费者模式
1） 线程的条件变量和线程锁
2） queue.Queue 队列 - 存储数据
3） 自定义同步的Queue
"""

from threading import Thread, current_thread, Condition, Lock
from queue import Queue

import time


class ConcurrentQueue():  # 同步队列 (线程安全)
    def __init__(self, max_size=10):
        self.max_size = max_size # 最大的容量
        self.queue = Queue()  # 仓库
        self.cond = Condition(Lock())

    def put(self, obj):
        # 将obj存入到仓库 - queue
        with self.cond:
            # 判断是否满仓
            while self.queue.qsize() >= self.max_size:
                self.cond.wait() # 阻塞，直到被其它线程唤醒 notify()

            self.queue.put(obj)
            # 唤醒消费者的线程
            self.cond.notify_all()

    def get(self):
        with self.cond:

            # 判断是否为空仓
            while self.queue.empty():
                self.cond.wait()

            obj = self.queue.get()
            self.cond.notify_all()  # 唤醒生产者线程

        return obj


num = 1  # 商品编号
num_lock = Lock()

def producer(q, delay):
    global num
    # 生产者线程
    # 间隔delay时间，生产商品
    while True:
        with num_lock:
            data = (current_thread().name, num)
            q.put(data)
            num += 1

        time.sleep(delay)


def consumer(q, delay):
    # 消费者线程
    while True:
        data = q.get()
        print(current_thread().name, '消费了', data)

        time.sleep(delay)


if __name__ == '__main__':
    queue = ConcurrentQueue(100)

    # 创建3个生产者线程
    producer_threads = [
        Thread(target=producer, args=(queue, 0.2))
        for _ in range(3)
    ]

    # 创建5个消费者线程
    consumer_threads = [
        Thread(target=consumer, args=(queue, 0.5))
        for _ in range(5)
    ]

    all_threads = producer_threads+consumer_threads

    # 启动所有线程
    for t in all_threads:
        t.start()

    # 启动所有线程
    for t in all_threads:
        t.join()
