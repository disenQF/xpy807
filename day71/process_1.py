# coding: utf-8
"""
进程： 为了启动一段程序，系统为它创建资源，并创建一个线程来启动程序.
       这个程序在Python中可以理解为一个函数，在Linux中可以理解一个命令。
"""

import random

import time

import multiprocessing

import os

"""
每隔一秒中生成一个6位由数字、大小字母组成的key
并写入到keystore.keys文件中
"""


def generate_key():
    # ord(str) 返回一个ASCII字符的ASCII值(10进制值)
    characters = list(range(ord('0'), ord('9'))) + \
                 list(range(ord('a'), ord('z'))) + \
                 list(range(ord('A'), ord('Z')))

    # chr(code) 返回ASCII值对应的ASCII字符
    characters = [chr(code) for code in characters]
    cs = ''.join([random.choice(characters) for _ in range(6)])
    return cs


def new_keys():
    while True:
        key = generate_key()
        # 获取当前函数执行时，所在的进程信息
        current_process = multiprocessing.current_process()

        # 进程的信息(进程ID,父进程、进程状态)
        pid = current_process.pid  # os.getpid()
        ppid = os.getppid() # 父进程的ID

        print('%s in %s ' % (pid, ppid), time.strftime('%d %H:%M:%S', time.localtime()), key)
        # 写入到keystore.keys文件
        # 常用的文件mode:  r, w, a, r+, w+, rb, wb, r+b, w+b, ab
        with open('keystore.keys', 'a') as file:
            file.write(key+"\n")

        time.sleep(1)


if __name__ == '__main__':
    # new_keys() # 将这个函数(任务/功能/程序)，放在(子)进程中执行
    # 1. 创建(子)进程
    # process = multiprocessing.Process(target=new_keys)
    process_list =[ multiprocessing.Process(target=new_keys) for _ in range(5)]

    # 2. 启动进程
    # process.start()  # 异步操作之后，当前的程序不会阻塞，则会继续向下执行
    for process in process_list:
        process.start()
    print('--正在生成--')  # 会先执行当前(父进程)的函数