# -*- coding: utf-8 -*-
# @Time    : 2021/7/31 12:10
# @Author  : wkRonin
# @File    :item_30.py
"""
不要让函数直接返回列表，应该让它逐个生成列表里的值(使用迭代器)
返回字符串里每个单词的首字母所对应的下标
"""


# 返回迭代器传到next函数中，每一次只处理一个单词，而不会占用很多内存
def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1


address = 'Four score and seven years ago...'
it = index_words_iter(address)
print(next(it))
print(next(it))
# 需要结果为列表的话
result = list(index_words_iter(address))
print(result[:10])


# 如果是一个很长的文件，迭代器可以接受长度任意的输入信息，并把内存消耗压得很低
def index_file(handle):
    offset = 0
    for line in handle:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == ' ':
                yield offset


address_lines = """Four score and seven years
ago our fathers brought forth on this
continent a new nation, conceived in liberty,
and dedicated to the proposition that all men
are created equal."""

with open('address.txt', 'w') as f:
    f.write(address_lines)

import itertools
with open('address.txt', 'r') as f:
    it = index_file(f)
    # itertools.islice(iterable, start, stop[, step])创建一个迭代器，返回从 iterable 里选中的元素
    results = itertools.islice(it, 0, 10)
    print(list(results))

