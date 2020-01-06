# coding=utf-8
import requests


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


def get_one_words(channel):
    """
    获取每日一句
    :param channel: 渠道
    :return: str,每日一句
    """
    d = {
        1: get_caihongpi_info,
        2: get_lovelive_info
    }
    if channel in d:
        return d[channel]()
    else:
        return None


if __name__ == '__main__':
    ow = get_one_words(3)
    print(ow)
    pass
