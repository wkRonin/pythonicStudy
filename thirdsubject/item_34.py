# -*- coding: utf-8 -*-
# @Time    : 2021/10/25 23:04
# @Author  : wkRonin
# @File    :item_34.py
"""
不要用send给生成器注入数据
"""
import math


# Example 1
def wave(amplitude, steps):
    """
    函数模拟正弦波，公式：f(x)=Asin(2pi/T)x   A为振幅，T为周期，x为x轴的变量，f(x)为y轴对应值
    :param amplitude: 振幅
    :param steps: 周期
    :return:
    """
    step_size = 2 * math.pi / steps
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        output = amplitude * fraction
        yield output


def transmit(output):
    if output is None:
        print(f"Output is None")
    else:
        print(f"Output: {output:>5.1f}")


def run(it):
    for output in it:
        transmit(output)


run(wave(3.0, 8))


# Example 2
def my_generator():
    received = yield 1
    print(f'received = {received}')


it = my_generator()
output = next(it)       # Get first generator output
print(f'output = {output}')

try:
    next(it)            # Run generator until it exits
except StopIteration:
    pass
else:
    assert False


# Example 3
it = my_generator()
output = it.send(None)  # Get first generator output
print(f'output = {output}')

try:
    it.send('hello!')   # Send value into the generator
except StopIteration:
    pass
else:
    assert False


# Example 4
def wave_modulating(steps):
    step_size = 2 * math.pi / steps
    amplitude = yield             # Receive initial amplitude
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        output = amplitude * fraction
        amplitude = yield output  # Receive next amplitude


def run_modulating(it):
    amplitudes = [
        None, 7, 7, 7, 2, 2, 2, 2, 10, 10, 10, 10, 10]
    for amplitude in amplitudes:
        output = it.send(amplitude)
        transmit(output)


run_modulating(wave_modulating(12))


# Example 5
def complex_wave():
    yield from wave(7.0, 3)
    yield from wave(2.0, 4)
    yield from wave(10.0, 5)


run(complex_wave())


# Example 6
def complex_wave_modulating():
    yield from wave_modulating(3)
    yield from wave_modulating(4)
    yield from wave_modulating(5)


run_modulating(complex_wave_modulating())


# Example 7
def wave_cascading(amplitude_it, steps):
    step_size = 2 * math.pi / steps
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        amplitude = next(amplitude_it)  # Get next input
        output = amplitude * fraction
        yield output


def complex_wave_cascading(amplitude_it):
    yield from wave_cascading(amplitude_it, 3)
    yield from wave_cascading(amplitude_it, 4)
    yield from wave_cascading(amplitude_it, 5)


def run_cascading():
    amplitudes = [7, 7, 7, 2, 2, 2, 2, 10, 10, 10, 10, 10]
    it = complex_wave_cascading(iter(amplitudes))
    for amplitude in amplitudes:
        output = next(it)
        transmit(output)


run_cascading()
