# -*- coding: utf-8 -*-
# @Time    : 2021/7/22 21:30
# @Author  : wkRonin
# @File    :item_21.py
"""
了解如何在闭包里面使用外围作用域中的变量
"""

numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 5, 3, 7}


# Example1
# 给列表排序，优先把群组之中的元素放在其他元素之前
def sort_priority(values, group):
    def helper(x):
        if x in group:
            return (0, x)
        return (1, x)
    values.sort(key=helper)


sort_priority(numbers, group)
print(numbers)


# Example2
# 增加返回： 列表里有没有位于群组之中的元素
def sort_priority2(values, group):
    # found ：外围作用域的变量无法被闭包函数改变
    found = False

    def helper(x):
        # 使用nonlocal说明 会去外围作用域查找此变量并可以赋值,但不能侵入模块级别的作用域
        nonlocal found
        if x in group:
            # values的数据如果在群组中 found为True
            found = True
            # values的数据如果在群组中则返回第一个数为0的元祖
            return (0, x)
        # values的数据如果不在群组中则返回第一个数为1的元祖
        return (1, x)
    # 把元祖赋值给key并排序：第一个数为0的元祖的数据就能排在前面
    values.sort(key=helper)
    return found


found = sort_priority2(numbers, group)
print(numbers)
print(found)


# Example3
# 如果nonlocal的用法比较复杂，可改用辅助类来封装状态
class Sorter:
    def __init__(self, group):
        self.group = group
        self.found = False

    # __call__ 方法参考第38条
    def __call__(self, x):
        if x in self.group:
            self.found = True
            return (0, x)
        return (1, x)


sorter = Sorter(group)
numbers.sort(key=sorter)
assert sorter.found is True
assert numbers == [2, 3, 5, 7, 1, 4, 6, 8]






