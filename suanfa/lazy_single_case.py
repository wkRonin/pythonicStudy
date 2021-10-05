# -*- coding: utf-8 -*-
# @Time    : 2021/10/5 23:31
# @Author  : wkRonin
# @File    :lazy_single_case.py
"""
懒汉式单例，在类使用阶段才会创建实例
"""
from threading import Lock


class IdMaker:

    # 申请一个线程锁
    __instance_lock = Lock()

    # python 的类变量会被多个类，实例共享
    __instance = None

    # __id 也是类变量，多个实例或类共享
    __id = -1

    # 如果 __new__ 抛出异常，就不允许调用者进行实例化
    def __new__(cls):

        raise ImportError("Instantition not allowed")

    # 类方法不用实例化也能调用，因为我们不允许进行实例化，所以要使用类方法
    @classmethod
    def get_instance(cls):

        # with 会帮我们自动的上锁和释放，不用我们操心
        with cls.__instance_lock:

            if cls.__instance is None:
                # 因为我们的 __new__ 代码不允许进行实例化，所以可以借用父类的 __new__ 进行实例化
                cls.__instance = super().__new__(cls)

        return cls.__instance

    # 计数器，在获取前，进行 + 1

    def get_id(self):

        self.__id += 1

        return self.__id


def test_id_maker():

    # IdMaker 是单例类，只允许有一个实例

    id1 = IdMaker.get_instance().get_id()

    id2 = IdMaker.get_instance().get_id()

    id3 = IdMaker.get_instance().get_id()

    print(id1, id2, id3)


if __name__ == "__main__":

    test_id_maker()

    # 0 1 2
