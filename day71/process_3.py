"""
基于Pipe的进程通信
1） 半双工
"""

from multiprocessing import Process, Pipe
import os

import time


def download(conn):
    # 从conn中读取下载的任务
    while True:
        # 从管道中接收数据
        url = conn.recv()  # receive()
        if url == 'over':
            break
        print(os.getpid(), url)


def start_requests(conn):
    # 通过conn发布下载的任务
    for url in ('http://www.baidu.com',
                'http://www.hao123.com',
                'http://www.qq.com'):
        conn.send(url)
        print(os.getpid(), '发布', url)
        time.sleep(1)

    conn.send('over') # 通信接收端，发完了，不用再接了


if __name__ == '__main__':
    # duplex 表示是否为全双工， False表示半双工
    # conn1 只收
    # conn2 只发
    conn1, conn2 = Pipe(duplex=False)

    # 创建发布下载任务的进程
    publisher = Process(target=start_requests, args=(conn2, ))

    # 创建接收下载任务的进程
    downloader = Process(target=download, args=(conn1, ))

    publisher.start()
    downloader.start()

    publisher.join()
    downloader.join()

    print('--over--')