# -*- coding: utf-8 -*-
# @Time    : 2021/10/21 21:57
# @Author  : wkRonin
# @File    :item_32.py
"""
考虑用生成器表达式改写数据量较大的列表推导
"""

# Example 1
import random

with open('my_file.txt', 'w') as f:
    for _ in range(10):
        f.write('a' * random.randint(0, 100))
        f.write('\n')

value = [len(x) for x in open('my_file.txt')]
print(value)

# Example 2
it = (len(x) for x in open('my_file.txt'))
print(it)

# Example 3
print(next(it))
print(next(it))

# Example 4
roots = ((x, x**0.5) for x in it)

# Example 5
print(next(roots))

