# -*- coding: utf-8 -*-
# @Time    : 2021/8/28 12:40
# @Author  : wkRonin
# @File    :ques0610.py
"""
题目：实现一个trim()函数，去除字符串首尾的空格（不能使用strip()方法）
例：
1.字符串为空的情况，输入trim(’ ‘)  预期返回结果 ‘’
2.字符串首尾空格数大于1的情况，输入trim(’  a bc    ') 预期返回结果  ‘a bc’
"""
import re

# 正则解法
def trim(s):
   return re.sub(r'^(\s+)|(\s+)$', '', s)


assert trim('abc') == 'abc'
assert trim('a b c') == 'a b c'
assert trim(' abc ') == 'abc'
assert trim('  abc') == 'abc'
assert trim('abc  ') == 'abc'
assert trim('  abc  ') == 'abc'
assert trim('  a  b  c  ') == 'a  b  c'


# 切片法
def trim2(s):
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[0:-1]
    return s


assert trim2('abc') == 'abc'
assert trim2('a b c') == 'a b c'
assert trim2(' abc ') == 'abc'
assert trim2('  abc') == 'abc'
assert trim2('abc  ') == 'abc'
assert trim2('  abc  ') == 'abc'
assert trim2('  a  b  c  ') == 'a  b  c'