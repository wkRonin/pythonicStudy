# -*- coding: utf-8 -*-
# @Time    : 2021/7/22 21:30
# @Author  : wkRonin
# @File    :item_20.py

"""
遇到意外情况时应该抛出异常
不要返回None
"""


def careful_divide(a: float, b: float) -> float:
    """Divides a by b.

    Raises:
        ValueError: When the inputs cannot be divided.
    """
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs')


try:
    result = careful_divide(1, 0)
    assert False
except ValueError:
    pass  # Expected

assert careful_divide(1, 5) == 0.2
