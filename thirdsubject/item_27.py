# -*- coding: utf-8 -*-
# @Time    : 2021/7/29 21:12
# @Author  : wkRonin
# @File    :item_27.py
"""
用列表推导式取代map与filter
"""
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 列表中每个元素的平方
squares = [x**2 for x in a]  # List comprehension
print(squares)

# 列表中偶数的平方
even_squares = [x**2 for x in a if x % 2 == 0]
print(even_squares)

# 字典推导
even_squares_dict = {x: x**2 for x in a if x % 2 == 0}
print(even_squares_dict)
threes_cubed_set = {x**3 for x in a if x % 3 == 0}
print(threes_cubed_set)


