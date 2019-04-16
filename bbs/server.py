# coding: utf-8
import socket
from multiprocessing import Process


def start_one(port):
    """
    一对一聊天服务器
    """
    server = socket.socket()
    server.bind(('', port))
    server.listen()
    client, address = server.accept()  # 等待连接
    print(address)
    client_ip = address[0]
    print('%s 已进入聊天室' % client_ip)
    msg = '%s 进入聊天室成功' % client_ip
    client.send(msg.encode())  # 发送的是字节码

    while True:
        msg = client.recv(8192)  # 每次接收数据的大小
        recv_msg = '%s: %s' %(client_ip, msg.decode())
        print(recv_msg)
        if msg == b'bye':
            break

        client.send(recv_msg.encode())

    print(client_ip, '退出了聊天室')


if __name__ == '__main__':
    print('staring bbs server ')
    process = Process(target=start_one,
                      args=(5001,))  # port (0, 65525)
    process.start()
    process.join()
    print('shutdown bbs server')
