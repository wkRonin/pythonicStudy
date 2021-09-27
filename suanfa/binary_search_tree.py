# -*- coding: utf-8 -*-
# @Time    : 2021/9/27 22:33
# @Author  : wkRonin
# @File    :binary_search_tree.py
"""
用列表实现二叉查找树的增，删，查
前序遍历、中序遍历、后序遍历
"""


class BinarySearchTree:
    class Node:
        def __init__(self, data) -> None:
            self.data = data
            self.left = None
            self.right = None

    def __init__(self) -> None:
        self.tree = None

    def insert(self, value):
        """
        实现二叉查找树的增
        :param value:插入的数据
        :return:
        """
        # 如果是根节点，直接插入
        if self.tree is None:
            self.tree = self.Node(value)
            return
        p = self.tree
        while p is not None:
            if value > p.data:
                if p.right is None:
                    p.right = self.Node(value)
                    return
                p = p.right
            elif value < p.data:
                if p.left is None:
                    p.left = self.Node(value)
                    return
                p = p.left

    def find(self, value):
        """
        实现二叉查找树的查
        :param value: 查找的数据
        :return:
        """
        p = self.tree
        while p is not None:
            if value > p.data:
                p = p.right
            elif value < p.data:
                p = p.left
            else:
                return p
        return None

    def delete(self, value):
        """
        实现二叉查找树的删
        :param value:删除的数据
        :return:
        """
        p = self.tree  # 当前节点
        pp = None      # p 的父节点
        # 循环查找要删的数据
        while p is not None and p.data != value:
            pp = p
            if value > p.data:
                p = p.right
            elif value < p.data:
                p = p.left

        # 没有找到要删的数据
        if p is None:
            return

        # 当前节点有两个孩子时
        if p.left is not None and p.right is not None:
            tmp_p = p.right  # 要删除的节点的右孩子
            tmp_pp = p  # 要删除的节点
            # 找要删除节点的右子树中的最小值
            while tmp_p.left is not None:
                tmp_pp = tmp_p
                tmp_p = tmp_p.left
            # 把最小值赋值给要删除的节点
            p.data = tmp_p.data
            # 由于需要删除最小值，走后续删除有一个孩子或没有孩子的方法
            # 把最小值设置成p，pp为它的父节点
            p = tmp_p
            pp = tmp_pp

        # 要删除的节点有一个孩子或者没有孩子都赋值给child
        if p.left is not None:
            child = p.left
        elif p.right is not None:
            child = p.right
        else:
            child = None

        # 要删除的节点没有父节点，就等于删除根节点，且根节点下只有一个孩子或者没有孩子
        if pp is None:
            # 直接把孩子赋值给树
            self.tree = child
        # 把孩子赋值给要删除节点的父节点，区分p是pp的左孩子还是右孩子
        elif pp.left is p:
            pp.left = child
        elif pp.right is p:
            pp.right = child

    def pre_order(self, node):
        """ 前序遍历 节点 -> 左子树 -> 右子树"""
        if node is None:
            return
        print(node.data)
        self.pre_order(node.left)
        self.pre_order(node.right)

    def in_order(self, node):
        """ 中序遍历 左子树 -> 节点 -> 右子树"""
        if node is None:
            return
        self.in_order(node.left)
        print(node.data)
        self.in_order(node.right)

    def post_order(self, node):
        """ 后序遍历  左子树 -> 右子树 -> 节点"""
        if node is None:
            return
        self.post_order(node.left)
        self.post_order(node.right)
        print(node.data)


def test_binary_search_tree():

    binary_search_tree = BinarySearchTree()
    data = [1, 10, 20, 40, 13]
    for i in data:
        binary_search_tree.insert(i)
    assert 20 == binary_search_tree.find(20).data
    binary_search_tree.delete(20)
    assert binary_search_tree.find(20) is None
    # 1 10 40 13
    binary_search_tree.pre_order(binary_search_tree.tree)
    print("-----------------------")
    # 1 10 13 40
    binary_search_tree.in_order(binary_search_tree.tree)
    print("-----------------------")
    # 13 40 10 1
    binary_search_tree.post_order(binary_search_tree.tree)


if __name__ == '__main__':
    test_binary_search_tree()
