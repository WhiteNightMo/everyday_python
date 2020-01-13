"""
    Created by xukai on 2019/12/24
"""
from datetime import datetime

from config import *
from utils.email import send_mail
from utils.helper import get_diff_time, init_logger
from utils.weather import get_weather_info
from utils.one_words import get_one_words

if __name__ == '__main__':
    logger = init_logger()

    # 获取一句彩虹屁
    words = get_one_words(WORDS_CHANNEL)
    # 获取天气信息
    is_tomorrow = IS_TOMORROW and datetime.now().hour >= 20
    weather = get_weather_info(CITY_NAME, is_tomorrow=is_tomorrow)
    # 天数
    diff_time = get_diff_time(START_DATE, START_DATE_MSG)
    # 爱称
    pet_name = MY_NAME

    # 合并消息
    send_msg = '\n'.join(x for x in [words, weather, diff_time, pet_name] if x)
    # 发送邮件
    send_mail(to=YOUR_NAME, receiver=MAIL_RECEIVERS, msg=send_msg)
    logger.info('\n------------------\n' + send_msg + '\n')
