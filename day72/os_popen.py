"""
通过os.popen()实现与操作系统进行交互
使用场景如下：
-  远程启动或关闭服务
-  远程获取服务的资源
"""
import csv
import os

if __name__ == '__main__':
    # 1. 执行OS命令
    cmd = os.popen('docker images')

    file = open('images.csv', 'w')

    # 2. 读取命令执行的结果
    result = cmd.read()
    result = result.split('\n')
    titles = result[0].split()

    writer = csv.DictWriter(file, fieldnames=titles)
    writer.writeheader()  # 写入标题（第一次）

    for line in result[1:]:
        row = line.split()
        if len(row) < 6:
            continue
        writer.writerow({
            'REPOSITORY': row[0],
            'TAG': row[1],
            'IMAGE': row[2],
            'ID': row[3],
            'CREATED': row[4]+' '+row[5],
            'SIZE': row[6]
        })

    file.close()
    print('--写入成功--')