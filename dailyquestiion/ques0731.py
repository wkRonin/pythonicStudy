# -*- coding: utf-8 -*-
# @Time    : 2021/7/31 10:30
# @Author  : wkRonin
# @File    :ques0731.py
"""
已知两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回 -1 。
当 needle 是空字符串时我们应当返回 0
示例：

输入：haystack = "hello", needle = "ll"
输出：2
题目难度：简单
题目来源：力扣（LeetCode）28
"""


# 使用内置方法find
def strStr(haystack: str, needle: str) -> int:
    if haystack is None or needle is None:
        return 0
    else:
        index = haystack.find(needle, 0)
        return index


assert strStr("hello", "ll") == 2
assert strStr("aaaaa", "bba") == -1
assert strStr("afsdf", "") == 0


# 不使用内置方法
def strStr1(haystack: str, needle: str) -> int:
    len_ned = len(needle)
    len_stack = len(haystack)
    j = 0
    for i in range(len_stack+1):  # 遍历haystack
        if i+len_ned < len_stack + 1:
            if haystack[i: i + len_ned] == needle:  # 判断needle字符串与haystack片段是否相等
                j = i
                break
        else:
            j = -1
            break
    return j


assert strStr1("hello", "ll") == 2
assert strStr1("aaaaa", "bba") == -1
assert strStr1("afsdf", "") == 0
