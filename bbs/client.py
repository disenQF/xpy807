"""
聊天室的客户端
1) 创建socket
2) 连接聊天室的服务器
3) 接收服务器的消息
4) 向服务器发送消息
"""

import socket
from multiprocessing import Process

def connect(host, port):
    print('开始连接服务器 %s:%s' % (host, port))
    client = socket.socket()
    client.connect((host, port))

    while True:
        msg = client.recv(8192)
        print(msg.decode())
        send_msg = input('我说:', ) # 注：不能在子进程中执行
        client.send(send_msg.encode())
        if send_msg == 'bye':
            break

    print('断开服务器')


if __name__ == '__main__':
    connect('localhost', 5003)
