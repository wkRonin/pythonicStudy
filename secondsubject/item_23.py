# -*- coding: utf-8 -*-
# @Time    : 2021/7/25 12:06
# @Author  : wkRonin
# @File    :item_23.py
"""
用关键字参数来表示可选的行为（**kwargs）
"""


# Example 1
def remainder(number, divisor):
    return number % divisor


assert remainder(20, 7) == 6
# 四种写法相同
remainder(20, 7)
remainder(20, divisor=7)
remainder(number=20, divisor=7)
remainder(divisor=7, number=20)

my_kwargs = {
    'number': 20,
    'divisor': 7,
}
# **加在字典前面，会让python把字典的键值亿关键字参数的形式传递
assert remainder(**my_kwargs) == 6
my_kwargs = {
    'divisor': 7,
}
assert remainder(number=20, **my_kwargs) == 6
my_kwargs = {
    'number': 20,
}
other_kwargs = {
    'divisor': 7,
}
assert remainder(**my_kwargs, **other_kwargs) == 6


# Example 2
def print_parameters(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} = {value}')


print_parameters(alpha=1.5, beta=9, gamma=4)


# Example 3
def flow_rate(weight_diff, time_diff,
              period=1, units_per_kg=1):
    """
    计算液体流入容量的速率 kg/秒
    :param weight_diff: 容器刻度差
    :param time_diff: 时间差
    :param period: 时间段 单位秒
    :param units_per_kg: 重量单位 kg
    :return:
    """
    return ((weight_diff * units_per_kg) / time_diff) * period


weight_diff = 0.5
time_diff = 3
# 可选关键字参数应根据应通过参数名传递
pounds_per_hour = flow_rate(weight_diff, time_diff,
                            period=3600, units_per_kg=2.2)
print(pounds_per_hour)


# 不应该以位置参数传递可选参数
pounds_per_hour = flow_rate(weight_diff, time_diff, 3600, 2.2)
print(pounds_per_hour)
