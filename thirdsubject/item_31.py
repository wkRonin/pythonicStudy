# -*- coding: utf-8 -*-
# @Time    : 2021/8/1 12:49
# @Author  : wkRonin
# @File    :item_31.py
"""
谨慎地迭代函数所收到的参数
计算列表中每一个数据占总和的百分比
"""
from collections.abc import Iterator

path = 'my_numbers.txt'
with open(path, 'w') as f:
    for i in (15, 35, 80):
        f.write('%d\n' % i)


# 可迭代的容器类，用来读取文件中的数据
class ReadVisits:
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)


def normalize_defensive(numbers):
    if isinstance(numbers, Iterator):  # check iterator
        raise TypeError('Must supply a container')
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


visits = [15, 35, 80]
percentages = normalize_defensive(visits)
assert sum(percentages) == 100.0

visits = ReadVisits(path)
percentages = normalize_defensive(visits)
assert sum(percentages) == 100.0


# 如果普通迭代器传给内置的iter函数，那么函数会把迭代器本身传给调用者，反之如果传来的是容器类型，那么iter函数就会返回一个新的迭代对象
# 所以如果是read_visits用normalize_defensive抛出异常
def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)


it = read_visits('my_numbers.txt')
try:
    normalize_defensive(it)
except TypeError:
    pass
else:
    assert False