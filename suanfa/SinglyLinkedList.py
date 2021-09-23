# -*- coding: utf-8 -*-
# @Time    : 2021/9/23 22:33
# @Author  : wkRonin
# @File    :SinglyLinkedList.py
"""
单链表
"""


class SinglyLinkedList():
    def __init__(self) -> None:
        self.head = None

    def insert_tail(self, value):
        if self.head is None:
            self.insert_to_head(value)
            return
        q = self.head
        # 寻找尾节点
        while q.next is not None:
            q = q.next
        new_node = self.Node(value)
        q.next = new_node

    def insert_to_head(self, value):
        new_node = self.Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def delete_by_value(self, value):
        if self.head is None:
            return False
        q = self.head
        # p 用来记录前驱结点
        p = None
        while q is not None and q.data != value:
            p = q
            q = q.next
        # 当链表中没有value的时候
        if q is None:
            return False
        # head 的值就是 value 的时候
        if p is None:
            self.head = self.head.next
        else:
            p.next = q.next
        return True

    def find_by_value(self, value):
        if self.head is None:
            return
        q = self.head
        while q is not None and q.data != value:
            q = q.next
        if q is None:
            return
        return q

    def insert_after(self, node, value):
        if node is None:
            return
        new_node = self.Node(value)
        new_node.next = node.next
        node.next = new_node

    def insert_before(self, node, value):
        if self.head is None:
            self.insert_to_head(value)
            return
        q = self.head
        while q is not None and q.next != node:
            q = q.next
        # 链表中 没有一个与node相等的节点
        if q is None:
            return
        new_node = self.Node(value)
        new_node.next = node
        q.next = new_node

    def print_all(self):
        if self.head is None:
            return
        q = self.head
        while q is not None:
            print(q.data)
            q = q.next

    class Node:
        def __init__(self, data) -> None:
            self.data = data
            self.next = None


def test_link():
    link = SinglyLinkedList()
    data = [1, 2, 5, 3, 1]
    for i in data:
        link.insert_tail(i)
    link.insert_to_head(99)
    # 打印内容为 99 1 2 5 3 1
    link.print_all()
    link.delete_by_value(2)
    assert not link.delete_by_value(999)
    assert link.delete_by_value(99)
    # 打印内容为 1 5 3 1
    link.print_all()
    assert link.find_by_value(2) is None
    new_node = link.find_by_value(3)
    link.insert_after(new_node, 10)
    assert link.find_by_value(3).next.data == 10
    link.insert_before(new_node, 30)
    assert link.find_by_value(5).next.data == 30


if __name__ == '__main__':
    test_link()
