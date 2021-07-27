# -*- coding: utf-8 -*-
# @Time    : 2021/7/27 21:03
# @Author  : wkRonin
# @File    :item_26.py
"""
用functools.wraps定义函数修饰器
不用此wraps定义自己的修饰器的话
会让那些利用introspection机制运作的工具（例如调试器，help函数，对象序列化器）产生奇怪的行为
"""
# 一开始不了解！r的意思通过此网站了解：https://www.cnblogs.com/baxianhua/p/10769958.html
import pickle
from functools import wraps


def trace(func):
    """ 使修饰器修饰的函数 执行每一次递归时
    打印输入的参数 以及返回的值
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}({args!r}, {kwargs!r}) '
              f'-> {result!r}')
        return result
    return wrapper


# 斐波那契数列方法
@trace
def fibonacci(n):
    """return the n-th fibonacci number"""
    if n in (0, 1):
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


fibonacci(4)
# 如果不用wraps定义修饰器会导致help打印出wrapper方法
help(fibonacci)
# 如果不用wraps定义修饰器会导致无法确定受修饰的那个原始函数的位置而导致报错
print(pickle.dumps(fibonacci))




