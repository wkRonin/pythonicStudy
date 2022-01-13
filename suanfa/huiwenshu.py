# -*- coding: utf-8 -*-
# @Time    : 2022/1/13 21:30
# @Author  : wkRonin
# @File    :huiwenshu.py
"""
给定一个整数 x ， 如果 x 是一个回文数（Palindrome）, 返回True,
否则返回False
回文数是指正序（从左向右）和倒叙（从右向左）都是一样的整数
例如：1221，12321，而1223不是
"""


# 第一种字符串逆转法
# def is_palindrome(x):
#     if x < 0 or x > 0 and x%10 == 0:
#         return False
#     str_x = str(x)
#     return str_x == str_x[::-1]


def is_palindrome(x):
    if x < 0 or x > 0 and x % 10 == 0:
        return False
    reverted = 0
    while x > reverted:
        reverted = reverted*10 + x % 10
        x //= 10
    return x == reverted or x == reverted//10


print(is_palindrome(5556655448445566555))
