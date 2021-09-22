# -*- coding: utf-8 -*-
# @Time    : 2021/9/22 22:23
# @Author  : wkRonin
# @File    :stackbaseonlinkedlist.py
"""
使用链表实现栈(链式栈)
入栈时间复杂度：O(1)
出栈时间复杂度：O(1)
"""


class StackBasedOnLinkedList:
    def __init__(self) -> None:
        self.top = None

    def push(self, value):
        new_node = self.Node(value)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if self.top is None:
            return -1
        result = self.top.data
        self.top = self.top.next
        return result

    class Node:
        def __init__(self, data) -> None:
            self.data = data
            self.next = None


def test_static():
    stack = StackBasedOnLinkedList()
    data = [1, 2, 3, 4, 5]
    for i in data:
        stack.push(i)
    data.reverse()
    for i in data:
        assert i == stack.pop()
    assert stack.pop() == -1