# coding: utf-8
"""
创建 Process时为target目标函数提供参数
任务： 由子进程完成keystore.keys文件的读取，每隔一秒读取一次
"""
from multiprocessing import Process
import os
import time


def read_key(filepath: str, timedelta: float) -> None:
    with open(filepath, 'r') as file:
        # 文件对象可被迭代
        for line in file:
            print(os.getpid(), line, end='')
            time.sleep(timedelta)

    print('%s 读取完成!' % filepath)


if __name__ == '__main__':
    # read_key('keystore.keys', 0.1)
    # process = Process(target=read_key,
    #                   args=('keystore.keys', 0.5))
    #
    # process.start()
    # process.join()  # 等待子进程执行完， 可能阻塞， 直到子进程执行完

    files = (('keystore.keys', 0.1),
             ('process_1.py', 0.2))

    # 批量创建进程
    process_list = [ Process(target=read_key,
                             kwargs=dict(filepath=filepath,
                                         timedelta=timedelta))
                     for filepath, timedelta in files]

    # 批量启动
    for process in process_list:
        process.start()

    # 批量等待子进程完成
    for process in process_list:
        process.join()

    print('---over---')
