# -*- coding: utf-8 -*-
# @Time    : 2021/7/29 21:24
# @Author  : wkRonin
# @File    :item_28.py
"""
控制推导逻辑的子表达式不要超两个
"""
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 二维列表转化成一维列表
flat = [x for row in matrix for x in row]
print(flat)

# 二维列表的每个元素的平方值
squared = [[x**2 for x in row] for row in matrix]
print(squared)

# 三维矩阵转成一维列表 不用推导式 否则多层循环的代码很难读懂
my_lists = [
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]],
]
for sublist1 in my_lists:
    for sublist2 in sublist1:
        flat.extend(sublist2)
print(flat)

# 各元素之和大于10且能被三整除
filtered = [[x for x in row if x % 3 == 0]
            for row in matrix if sum(row) >= 10]
print(filtered)