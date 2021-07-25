# -*- coding: utf-8 -*-
# @Time    : 2021/7/25 12:30
# @Author  : wkRonin
# @File    :item_24.py
"""
用None和docstring来描述默认值会变的参数
"""
from time import sleep
from datetime import datetime


# Example 1
def log(message, when=None):
    """Log a message with a timestamp.

    Args:
        message: Message to print.
        when: datetime of when the message occurred.
            Defaults to the present time.
    """
    if when is None:
        when = datetime.now()
    print(f'{when}: {message}')


# 函数中when默认值不设置为None的话会只执行一次datetime.now()一次
log('Hi there!')
sleep(0.1)
log('Hello again!')


# Example 2
import json


def decode(data, default=None):
    """
    将字符串转化成字典
    :param data:需解码的字符串
    :param default:返回的默认值
    :return:如果解码失败返回空字典
    """
    try:
        return json.loads(data)
    except ValueError:
        if default is None:
            default = {}
        return default


foo = decode('aaa')
foo['stuff'] = 5
bar = decode('bbb')
bar['meep'] = 1
print('Foo:', foo)
print('Bar:', bar)
assert foo is not bar


# Example 3
from typing import Optional


def log_typed(message: str,
              when: Optional[datetime] = None) -> None:
    """
    日志记录message前打印时间戳
    :param message: 打印的信息
    :param when: 标注成可选值（Optional）,并限定其类型为datetime
    :return: when ： message
    """
    if when is None:
        when = datetime.now()
    print(f'{when}: {message}')


log_typed("Hello")
sleep(0.1)
log_typed('Hello again!')
