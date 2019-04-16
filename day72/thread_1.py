"""
第一个Python的线程使用
用法基本和进程相同，使用threading库
步骤：
- 使用threading.Thread类，创建线程对象
- 通过线程对象启动线程 - start()
- 通过线程对象调用.join() 等待线程完成
"""

import threading
import csv

import time

# 注：多线程是共享同一进程的内存空间
is_stop = False  # 停止读取线程的标识， 变量可以用在多个子线程中


def read_csv(filepath):
    """
    读取csv文件中的数据，每隔一秒中显示一行
    :param filepath: 文件路径
    :return:
    """
    with open(filepath, 'r') as file:
        reader = csv.DictReader(file,
                                fieldnames=('REPOSITORY','TAG','IMAGE','ID','CREATED','SIZE'))
        for row in reader:
            # 通过标识位的方式中断线程
            if is_stop: break
            # 获取当前线程的名称
            thread_name = threading.current_thread().name
            print(thread_name, row)
            time.sleep(1)


def delay_stop(delay):
    # 延迟delay多长时间之后，尝试关闭子线程
    print(threading.current_thread().name, '延迟 %s 来中断读取线程' % delay)
    time.sleep(delay)
    global is_stop
    is_stop = True


if __name__ == '__main__':
    # 1. 创建线程对象
    # Thread()中参数同Process()中参数
    thread = threading.Thread(target=read_csv,
                              args=('images.csv', ))

    # 2. 启动线程
    thread.start()  # 异步执行
    print(threading.current_thread().name, '---正在读取csv文件--')

    # 启动延迟中断读取csv的线程
    threading.Thread(target=delay_stop,
                     args=(5, )).start()

    # 3. 等待子线程执行完成
    thread.join()  # 同步执行， 阻塞到线程执行完

    # ?? 如果线程在运行的情况下，如果中断线程
    # thread.is_alive()  判断线程是否存活
    # 可以使用标识符号

    print('--over--')