# -*- coding: utf-8 -*-
# @Time    : 2021/10/27 21:53
# @Author  : wkRonin
# @File    :item_35.py
"""
不要通过throw变换生成器的状态（会变的难以理解）
"""
import logging

# Example 1
try:
    class MyError(Exception):
        pass


    def my_generator():
        yield 1
        yield 2
        yield 3


    it = my_generator()
    print(next(it))  # Yield 1
    print(next(it))  # Yield 2
    print(it.throw(MyError('test error')))
except:
    logging.exception('Expected')
else:
    assert False


# Example 2
def my_generator():
    yield 1

    try:
        yield 2
    except MyError:
        print('Got MyError!')
    else:
        yield 3

    yield 4

it = my_generator()
print(next(it))  # Yield 1
print(next(it))  # Yield 2
print(it.throw(MyError('test error')))


# Example 3
class Reset(Exception):
    pass


def timer(period):
    current = period
    while current:
        current -= 1
        try:
            yield current
        except Reset:
            current = period


# Example 4
RESETS = [
    False, False, False, True, False, True, False,
    False, False, False, False, False, False, False]


def check_for_reset():
    # Poll for external event
    return RESETS.pop(0)


def announce(remaining):
    print(f'{remaining} ticks remaining')


def run():
    it = timer(4)
    while True:
        try:
            if check_for_reset():
                current = it.throw(Reset())
            else:
                current = next(it)
        except StopIteration:
            break
        else:
            announce(current)


run()


# Example 5
class Timer:
    def __init__(self, period):
        self.current = period
        self.period = period

    def reset(self):
        self.current = self.period

    def __iter__(self):
        while self.current:
            self.current -= 1
            yield self.current


def run():
    timer = Timer(4)
    for current in timer:
        if check_for_reset():
            timer.reset()
        announce(current)


run()
