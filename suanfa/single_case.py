# -*- coding: utf-8 -*-
# @Time    : 2021/10/5 23:27
# @Author  : wkRonin
# @File    :single_case.py
"""
饿汉式单例，在类加载时就创建好实例
"""


class IdMaker:

    # python 的类变量会被多个类，实例共享

    __instance = None

    # __id 也是类变量，多个实例或类共享

    __id = -1

    # python 在类加载阶段，通过父类的 __new__ 创建实例，如果我们重写 __new__

    # 就不会调用父类的 __new__ ，就会调用我们写的 __new__ 创建实例

    # __new__ 需要返回一个实例，如果不返回，就不会实例化

    def __new__(cls):

        if cls.__instance is None:

            # 父类的 __new__ ，参数接收一个类名，会返回类的实例

            cls.__instance = super().__new__(cls)

        return cls.__instance

    # 计数器，在获取前，进行 + 1

    def get_id(self):

        self.__id += 1

        return self.__id

def test_id_maker():

    # IdMaker 是单例类，只允许有一个实例

    id1 = IdMaker().get_id()

    id2 = IdMaker().get_id()

    id3 = IdMaker().get_id()

    print(id1, id2, id3)


if __name__ == "__main__":

    test_id_maker()

    # 0 1 2
