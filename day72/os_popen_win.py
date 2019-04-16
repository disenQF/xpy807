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
    cmd = os.popen('dir -la')

    # 2. 读取命令执行的结果
    result = cmd.read()

    # 3. 分析和处理数据
    print(result)