# coding: utf-8
import socket
from multiprocessing import Process, Queue
from threading import Thread, Lock


def session(client, client_ip, all_client, lock):
    """
    管理某一个socket连接
    1) 读取client中的数据
    2）向所有已连接的client发送的数据
    """
    print('%s 已进入聊天室' % client_ip)
    msg = '%s 进入聊天室成功' % client_ip

    # 向所有客户端发送信息
    for c in all_client:
        c.send(msg.encode())  # 发送的是字节码

    while True:
        msg = client.recv(8192)  # 每次接收数据的大小
        recv_msg = '%s: %s' % (client_ip, msg.decode())
        print(recv_msg)
        if msg == b'bye':
            break

        # 向所有客户端发送信息
        for c in all_client:
            c.send(recv_msg.encode())  # 发送的是字节码

    with lock:
        all_client.remove(client)

    print(client_ip, '退出了聊天室')

def start_multi(port):
    """
    多人聊天服务器
    """
    server = socket.socket()
    server.bind(('', port))
    server.listen()

    clients = []
    lock = Lock()
    while True:
        client, address = server.accept()  # 等待连接
        with lock:
            clients.append(client)  # 将当前连接的client添加到列表中

        Thread(target=session,
                args=(client, address[0], clients, lock)).start()


if __name__ == '__main__':
    print('staring bbs server ')
    process = Process(target=start_multi,
                      args=(5003,))  # port (0, 65525)
    process.start()
    process.join()
    print('shutdown bbs server')
