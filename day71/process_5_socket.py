"""
基于socket实现进程间通信
# 要求： 通过.socket文件实现的
"""

from multiprocessing import Process
import socket
import os
import time

def download(url, socket_filepath):
    print(os.getpid(), 'start request ', url)
    time.sleep(2)
    data = '%s:%s' % (url, '<html><h1>hi</h1></html>')

    # 将data数据写入scoket中，传递给parser进程
    s = socket.socket(socket.AF_UNIX)

    # 直到 socket_filepath文件存在为此
    while not os.path.exists(socket_filepath):
        pass

    s.connect(socket_filepath)
    # 将数据写入socket
    s.send(data.encode())
    print(os.getpid(), '---发送数据成功--')


def parse(socket_filepath):
    s = socket.socket(socket.AF_UNIX)
    if os.path.exists(socket_filepath):
        os.remove(socket_filepath)

    s.bind(socket_filepath) # 绑定socket文件
    s.listen()
    c, address = s.accept() # 等待连接
    data = c.recv(1024*8)  # 接收连接进程的数据
    print(os.getpid(), data)


if __name__ == '__main__':
    # 指定两个进程间通信的socket文件
    socket_file = 'process5.socket'

    downloader = Process(target=download,
                         args=('http://www.baidu.com', socket_file))

    parser = Process(target=parse,
                     args=(socket_file, ))
    downloader.start()
    parser.start()

    downloader.join()
    parser.join()

    print(os.getpid(), '----over----')

