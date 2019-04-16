"""
线程的本地变量
问题描述：
1） 多线程中访问的公共的变量都是共享同一内存的，
2） 如果使用同一名字，且作用范围只限于本线程的话，只能使用本地变量

v=local() 线程本地变量的用法
1） 每个线程中的变量，类似于dict结构，key是当前线程对象
2） v.money = 0  向v中添加一个线程本地变量
"""
import random
from threading import Thread, current_thread, local

import time

v = local()  # 创建线程的本地变量
v.money = 1000


def new_add(m):
    global v
    print(current_thread().name, '准备开户: ')
    v.money = 0  # 向本地变量中添加一个money

    """开户、并存钱m """
    print(current_thread().name,
          '存入 %s 钱' % m, '余额 %s 钱' % v.money)
    v.money += m
    time.sleep(1)
    print(current_thread().name,
          '余额 %s 钱' % v.money)


if __name__ == '__main__':
    # 模拟10人开户并存钱
    add_threads = [
        Thread(target=new_add,
               args=(random.randint(100, 1000), ))
        for _ in range(10)
    ]

    for t in add_threads:
        t.start()

    for t in add_threads:
        t.join()

    print(current_thread().name,
          '余额 %s 钱' % v.money)