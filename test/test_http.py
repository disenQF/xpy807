import socket



s = socket.socket()
# 经过3次握手之后，确定是否成功
s.connect(('www.hao123.com', 80))
print('--连接成功')

headers = b"GET / HTTP/1.1\nHost: www.hao123.com\n\n"
s.send(headers)
while True:
    resp_data = s.recv(1024)
    # b'HTTP/1.1 200 OK\r\nConnection: keep-alive\r\n
    print(resp_data)
    if resp_data == b'':
        break