# coding=utf-8
import random

import requests

from utils.helper import is_json


def get_caihongpi_info():
    """
    彩虹屁生成器
    :return: str,彩虹屁
    """
    print('获取彩虹屁信息...')
    try:
        resp = requests.get('https://chp.shadiao.app/api.php')
        if resp.status_code == 200:
            return resp.text
        print('彩虹屁获取失败。')
    except requests.exceptions.RequestException as exception:
        print(exception)
        # return None
    # return None


def get_lovelive_info():
    """
    从土味情话中获取每日一句
    :return: str,土味情话
    """
    print('获取土味情话...')
    try:
        resp = requests.get('https://api.lovelive.tools/api/SweetNothings')
        if resp.status_code == 200:
            return resp.text
        print('土味情话获取失败。')
    except requests.exceptions.RequestException as exception:
        print(exception)
        # return None
    return None


def get_acib_info():
    """
    从词霸中获取每日一句，带英文。
    :return: str,返回每日一句（双语）
    """
    print('获取格言信息（双语）...')
    try:
        resp = requests.get('http://open.iciba.com/dsapi')
        if resp.status_code == 200 and is_json(resp):
            content_dict = resp.json()
            content = content_dict.get('content')
            note = content_dict.get('note')
            return '{}{}'.format(content, note)

        print('没有获取到格言数据。')
    except requests.exceptions.RequestException as exception:
        print(exception)
    return None


def get_hitokoto_info():
    """
    从『一言』获取信息。(官网：https://hitokoto.cn/)
    :return: str,一言。
    """
    print('获取一言...')
    try:
        resp = requests.get('https://v1.hitokoto.cn/', params={'encode': 'text'})
        if resp.status_code == 200:
            return resp.text
        print('一言获取失败。')
    except requests.exceptions.RequestException as exception:
        print(exception)
        # return None
    # return None


def get_zsh_info():
    """
    句子迷：（https://www.juzimi.com/）
    朱生豪：https://www.juzimi.com/writer/朱生豪
    爱你就像爱生命（王小波）：https://www.juzimi.com/article/爱你就像爱生命
    三行情书：https://www.juzimi.com/article/25637
    :return: str,情话
    """
    print('正在获取民国情话...')
    try:
        name = [
            ['writer/朱生豪', 38],
            ['article/爱你就像爱生命', 22],
            ['article/25637', 55],
        ]
        apdix = random.choice(name)
        # page 从零开始计数的。
        url = 'https://www.juzimi.com/{}?page={}'.format(
            apdix[0], random.randint(1, apdix[1]))
        # print(url)
        resp = requests.get(url)
        if resp.status_code == 200:
            # print(resp.html)
            # results = resp.find('a.xlistju')
            # if results:
            #     re_text = random.choice(results).text
            #     if re_text and '\n\n' in re_text:
            #         re_text = re_text.replace('\n\n','\n')
            #     return re_text
            return None
        print('获取民国情话失败..')
    except Exception as exception:
        print(exception)
    return None


def get_one_words(channel):
    """
    获取每日一句
    :param channel: 渠道
    :return: str,每日一句
    """
    d = {
        1: get_caihongpi_info,
        2: get_lovelive_info,
        3: get_acib_info,
        4: get_hitokoto_info,
        # 5: get_zsh_info,
    }
    if channel not in d:
        channel = random.choice(list(d.keys()))
    return d[channel]()


if __name__ == '__main__':
    ow = get_one_words(3)
    print(ow)
    pass
