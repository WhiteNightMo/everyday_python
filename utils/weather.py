"""
    Created by xukai on 2019/12/24
"""
import requests
import json
import os
from datetime import datetime

with open(os.path.join(os.path.dirname(__file__), '_city_sojson.json'), 'r', encoding='utf-8') as f:
    CITY_CODE_DICT = json.loads(f.read())

MSG_TODAY = '{_date},{week} {city_name}\n【今日天气】{_type}\n【今日气温】{low_temp} {high_temp}\n【今日风速】{speed}\n【出行提醒】{notice}'


def get_sojson_weather(city_name):
    """
     获取天气信息。网址：https://www.sojson.com/blog/305.html .
    :param city_name: str,城市名
    :return: str ,例如：2019-06-12 星期三 晴 南风 3-4级 高温 22.0℃ 低温 18.0℃ 愿你拥有比阳光明媚的心情
    """
    if not city_name:
        return None
    city_code = CITY_CODE_DICT.get(city_name, None)
    if not city_code:
        print('没有此城市的消息...')
        return None
    print('获取天气信息...')

    weather_url = 'http://t.weather.sojson.com/api/weather/city/{}'.format(city_code)
    try:
        resp = requests.get(url=weather_url)
        if resp.status_code == 200:
            # print(resp.text)
            weather_dict = resp.json()
            # 今日天气
            # {
            # "sunrise": "04:45",
            # "high": "高温 34.0℃",
            # "low": "低温 25.0℃",
            # "sunset": "19:37",
            # "aqi": 145,
            # "ymd": "2019-06-12",
            # "week": "星期三",
            # "fx": "西南风",
            # "fl": "3-4级",
            # "type": "多云",
            # "notice": "阴晴之间，谨防紫外线侵扰"
            # }
            if weather_dict.get('status') == 200:

                today_weather = weather_dict.get('data').get('forecast')[0]

                today_date = datetime.now().strftime('%Y-%m-%d')
                # 这个天气的接口更新不及时，有时候当天1点的时候，还是昨天的天气信息，如果天气不一致，则取下一天(今天)的数据
                weather_today = today_weather['ymd']
                if today_date != weather_today:
                    today_weather = weather_dict.get('data').get('forecast')[1]

                weather_info = MSG_TODAY.format(
                    city_name=city_name,
                    _date=today_weather['ymd'],
                    week=today_weather['week'],
                    _type=today_weather['type'],
                    low_temp=today_weather['low'],
                    high_temp=today_weather['high'],
                    speed=today_weather['fx'] + today_weather['fl'],
                    notice=today_weather['notice'],
                )
                return weather_info
            else:
                print('天气请求出错:{}'.format(weather_dict.get('message')))

    except Exception as exception:
        print(str(exception))
        return None


def get_weather_info(city_name):
    """
    获取天气
    :param city_name:str,城市名称
    :return: str,天气情况
    """
    if not city_name:
        return
    return get_sojson_weather(city_name)


if __name__ == '__main__':
    ow = get_weather_info('上海')
    print(ow)
    pass
