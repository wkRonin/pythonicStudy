# -*- coding: utf-8 -*-
# @Time    : 2021/7/25 11:59
# @Author  : wkRonin
# @File    :item_22.py
"""
用数量可变的的位置参数给函数设计清晰的参数列表
"""


# Example 1
def log1(message, *values):
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print(f'{message}: {values_str}')


log1('My numbers are', 1, 2)
log1('Hi there')
favorites = [7, 33, 99]
log1('Favorite colors', *favorites)


# Example 2
def my_generator():
    for i in range(10):
        yield i


def my_func(*args):
    print(args)


it = my_generator()
my_func(*it)


# Example 3
# 给接受*args的函数添加新位置参数，可能导致难以排查的Bug
# 这是一个错误例子
def log2(sequence, message, *values):
    if not values:
        print(f'{sequence} - {message}')
    else:
        values_str = ', '.join(str(x) for x in values)
        print(f'{sequence} - {message}: {values_str}')

log2(1, 'Favorites', 7, 33)      # New with *args OK
log2(1, 'Hi there')              # New message only OK
log2('Favorite numbers', 7, 33)  # Old usage breaks