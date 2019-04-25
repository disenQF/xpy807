import logging
from logging import Formatter, StreamHandler, FileHandler
from logging.handlers import HTTPHandler

import sys

def init_logger():
    # 创建 scrapy 日志记录器
    logger = logging.getLogger('scrapy')
    logger.setLevel(logging.INFO)

    # 设置日志的格式化对象
    # 要求收集日志的时间、等级名称、发生所在的函数名及行号
    fmt_str = '%(asctime)s %(levelname)s %(funcName)s %(lineno)s: %(message)s'
    formatter = Formatter(fmt=fmt_str,
                          datefmt='%Y-%m-%d %H:%M:%S')

    handler1 = StreamHandler()
    handler1.setLevel(logging.INFO)
    handler1.setFormatter(formatter)

    handler2 = FileHandler('errors.log', encoding='utf-8')
    handler2.setLevel(logging.ERROR)
    handler2.setFormatter(formatter)

    handler3 = HTTPHandler(host='10.12.152.218:5000',
                           url='/log/',
                           method='POST')
    # handler3.setFormatter(formatter)
    handler3.setLevel(logging.ERROR)

    # 将处理器添加到日志记录器中
    logger.addHandler(handler1)
    logger.addHandler(handler2)
    logger.addHandler(handler3)


def test_logger():
    logger = logging.getLogger('scrapy')
    logger.info('产生了info的信息，haha')
    logger.debug('产生了debug信息，^__^')
    logger.critical('产生了critical信息， o_o')

    with open('abc.txt', 'r') as f:
        pass


# 自定义sys异常处理的勾子函数
def handle_global_except(except_type, except_val, except_tb):
    logger = logging.getLogger('scrapy')
    logger.error(except_val)


if __name__ == '__main__':
    # 如果程序抛出的异常没有被处理，则会由sys的解释器来处理
    # sys解析器处理异常的函数是 excepthook
    sys.excepthook = handle_global_except

    init_logger()
    test_logger()


