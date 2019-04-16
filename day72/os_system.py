"""
使用os.system来执行操作系统的命令
- 创建子进程来执行OS的命令
- 通过 sys.argv 接收命令行中的参数
"""
import os
import sys

if __name__ == '__main__':
    # 读取命令行的参数
    """
    命令行格式： 
    > python os_system.py filepath
    """
    # print(sys.argv)
    # if len(sys.argv) <= 1:
    #     raise Exception('必须指定读取的文件名参数')
    #
    # filepath = sys.argv[1]
    # Linux命令统计文件的行数
    # cat ../day71/keystore.keys |wc -l
    # os.system('cat %s |wc -l' % filepath)
    # os.system('notepad %s ' % filepath)  # window
    os.system('ls -la ..')

