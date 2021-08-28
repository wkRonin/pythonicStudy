# -*- coding: utf-8 -*-
# @Time    : 2021/8/28 13:24
# @Author  : wkRonin
# @File    :ques0613.py
"""
删除list 里面的重复元素 并保持顺序不变化
例 [1,2,4,2,4,3] 变成 [1,2,4,3]
"""


def single_num_list(test_list: list):
    i = 0
    while i < len(test_list):
        if test_list[i] in test_list[0:i]:
            test_list.pop(i)
        else:
            i += 1
    return test_list


assert single_num_list([1, 2, 4, 2, 4, 3]) == [1, 2, 4, 3]
assert single_num_list([1, 2, 2, 2, 2, 1]) == [1, 2]
assert single_num_list([]) == []
