"""
    Created by xukai on 2019/12/24
"""
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr, parseaddr

from config import *
from utils.helper import get_diff_time


def send_mail(to, receiver, msg):
    """
    发送邮件
    :param to: 接收人
    :param receiver: 接收邮箱
    :param msg: 邮件内容
    :return:
    """
    message = MIMEText(msg, 'plain', 'utf-8')
    message['From'] = _format_addr(MY_NAME + ' <%s>' % MAIL_USERNAME)
    # 群发则不解析收件人地址
    if isinstance(receiver, list) and len(receiver) > 1:
        message['To'] = Header(to, 'utf-8')
    else:
        receiver = receiver[0] if isinstance(receiver, list) else receiver
        message['To'] = _format_addr(to + ' <%s>' % receiver)
    message['Subject'] = Header(MAIL_SUBJECT_PREFIX + get_diff_time(START_DATE, START_DATE_MSG), 'utf-8')

    try:
        smtp = smtplib.SMTP(MAIL_SERVER, MAIL_PORT)
        smtp.login(MAIL_USERNAME, MAIL_PASSWORD)
        smtp.sendmail(MAIL_USERNAME, receiver, message.as_string())
        smtp.quit()
        print("邮件发送成功~")
    except smtplib.SMTPException as e:
        print("Error: 无法发送邮件")
        print(e)


def _format_addr(s):
    """自定义处理邮件收发地址的显示内容"""
    name, addr = parseaddr(s)
    print(name)
    print(addr)

    # 将邮件的name转换成utf-8格式，addr如果是unicode，则转换utf-8输出，否则直接输出addr
    return formataddr((Header(name, 'utf-8').encode(), addr))
