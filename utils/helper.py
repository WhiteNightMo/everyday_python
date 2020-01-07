"""
    Created by xukai on 2019/12/24
"""
import logging
import os
import re
import sys
from datetime import datetime


def get_diff_time(start_date, start_msg=''):
    """
    # 在一起，一共多少天了。
    :param start_date:str,日期
    :param start_msg:
    :return: str,eg（宝贝这是我们在一起的第 111 天。）
    """
    if not start_date:
        return None
    rdate = r'^[12]\d{3}[ \/\-](?:0?[1-9]|1[012])[ \/\-](?:0?[1-9]|[12][0-9]|3[01])$'
    start_date = start_date.strip()
    if not re.search(rdate, start_date):
        print('日期填写出错..')
        return
    start_datetime = datetime.strptime(start_date, '%Y-%m-%d')
    day_delta = (datetime.now() - start_datetime).days + 1
    if start_msg and start_msg.count('{}') == 1:
        delta_msg = start_msg.format(day_delta)
    else:
        delta_msg = '宝贝这是我们在一起的第 {} 天。'.format(day_delta)
    return delta_msg


def init_logger():
    path = r"./logs/"
    if not os.path.exists(path):
        os.makedirs(path)
    path += datetime.now().strftime('%Y-%m-%d') + ".log"

    logger = logging.getLogger('log')
    logger.setLevel(logging.DEBUG)

    # 调用模块时,如果错误引用，比如多次调用，每次会添加Handler，造成重复日志，这边每次都移除掉所有的handler，后面在重新添加，可以解决这类问题
    while logger.hasHandlers():
        for i in logger.handlers:
            logger.removeHandler(i)

    # file log
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh = logging.FileHandler(path, encoding='utf-8')
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    # console log
    formatter = logging.Formatter('%(message)s')
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger
