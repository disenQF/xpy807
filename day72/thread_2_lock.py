"""
因为多线程是共享内存的，
如果多个线程同时操作一个变量或对象时，
可能会发生脏数据或缺失
"""
from threading import Thread, current_thread, Lock

import time

money = 1000
lock = Lock()

def add(m):
    global money
    # 存入m 的钱数
    with lock:
        print(current_thread().name,
              '当前的余额：', money,
              '本次存放：', m)

        money += m
        time.sleep(1)
        print(current_thread().name,
              '存入后的金额：', money)


def sub(m):
    global money
    # 取 m的钱数

    # 进入上下文时，调用对象(lock)的__enter__函数 -> lock.acquire()
    # 退出上下文时，调用对象（lock）的__exit__函数 -> lock.release()
    with lock:
        print(current_thread().name,
              '当前的余额：', money,
              '本次取出：', m)

        money -= m
        time.sleep(1)

        print(current_thread().name,
              '取出后的金额：', money)


if __name__ == '__main__':
    # 模拟3人存钱， 2人取钱
    add_threads = [
        Thread(target=add, args=(m, ))
        for m in (1000, 2000, 3000)
    ]

    sub_threads = [
        Thread(target=sub, args=(m, ))
        for m in (500, 2500)
    ]

    for thread in add_threads + sub_threads:
        thread.start()

    for thread in add_threads + sub_threads:
        thread.join()

    print('最终的余额： %s' % money)