# -*- coding: utf-8 -*-
# @Time    : 2021/10/21 22:25
# @Author  : wkRonin
# @File    :item_33.py
"""
通过yield from 把多个生成器连起来用
"""


# Example 1
def move(period, speed):
    for _ in range(period):
        yield speed


def pause(delay):
    for _ in range(delay):
        yield 0


def animate_composed():
    yield from move(4, 5.0)
    yield from pause(3)
    yield from move(2, 3.0)


def render(delta):
    print(f'Delta: {delta:.1f}')


def run(func):
    for delta in func():
        render(delta)


run(animate_composed)


# Example 2
import timeit

def child():
    for i in range(1_000_000):
        yield i

def slow():
    for i in child():
        yield i

def fast():
    yield from child()

baseline = timeit.timeit(
    stmt='for _ in slow(): pass',
    globals=globals(),
    number=50)
print(f'Manual nesting {baseline:.2f}s')

comparison = timeit.timeit(
    stmt='for _ in fast(): pass',
    globals=globals(),
    number=50)
print(f'Composed nesting {comparison:.2f}s')

reduction = -(comparison - baseline) / baseline
print(f'{reduction:.1%} less time')
