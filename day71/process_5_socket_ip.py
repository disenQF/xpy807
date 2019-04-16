"""
基于socket实现进程间通信
# 要求： 通过(ip, port) 网络通信
"""

from multiprocessing import Process
import socket
import os
import time

def download(url, port):
    print(os.getpid(), 'start request ', url)
    time.sleep(2)
    data = '%s:%s' % (url, '<html><h1>hi</h1></html>')

    # 将data数据写入scoket中，传递给parser进程
    s = socket.socket()

    s.connect(('localhost', port))
    # 将数据写入socket
    s.send(data.encode())
    print(os.getpid(), '---发送数据成功--')


def parse(port):
    s = socket.socket(socket.AF_INET)
    s.bind(('', port)) # 绑定socket文件
    s.listen()
    c, address = s.accept() # 等待连接
    data = c.recv(1024*8)  # 接收连接进程的数据
    print(os.getpid(), data)


if __name__ == '__main__':

    downloader = Process(target=download,
                         args=('http://www.baidu.com', 8999))

    parser = Process(target=parse,
                     args=(8999, ))
    downloader.start()
    parser.start()

    downloader.join()
    parser.join()

    print(os.getpid(), '----over----')

