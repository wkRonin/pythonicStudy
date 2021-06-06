# -*- coding: utf-8 -*-
# @Time    : 2021/5/29 14:24
# @Author  : wkRonin
# @File    : item19.py
# @Software: PyCharm
from collections import namedtuple
# 不要把函数返回的多个数值拆分到三个以上的变量
# gitee改邮箱后测试连接


lengths = [63, 73, 72, 60, 67, 66, 71, 61, 72, 70]


def get_avg_ratio(numbers):
    """
    计算列表中每个值除以平均数的占比并降序排列
    :param numbers: 一个纯数字的列表
    :return: 计算后的降序列表
    """
    average = sum(numbers) / len(numbers)
    scaled = [x / average for x in numbers]
    scaled.sort(reverse=True)
    return scaled


# 用带*的表达式接收那些没有被普通变量捕获到的值
longest, *middle, shortest = get_avg_ratio(lengths)

# 格式化符号可参考官方文档https://docs.python.org/3/library/string.html
print(f'Longest:  {longest:>4.0%}')
print(f'Shortest: {shortest:>4.0%}')


# 错误方法,这种方法容易搞错顺序，最好定义一个轻便的类或namedtuple
def get_stats_f(numbers):
    """
    计算最小值，最大值，列表数值的数量，平均数，中位数
    :param numbers: 一个纯数字的列表
    :return: 返回一个五个数据的元祖，包含minimum, maximum, average, median, count
    """
    minimum = min(numbers)
    maximum = max(numbers)
    count = len(numbers)
    average = sum(numbers) / count

    sorted_numbers = sorted(numbers)
    middle = count // 2
    if count % 2 == 0:
        lower = sorted_numbers[middle - 1]
        upper = sorted_numbers[middle]
        median = (lower + upper) / 2
    else:
        median = sorted_numbers[middle]

    return minimum, maximum, average, median, count


minimum, maximum, average, median, count = get_stats_f(lengths)
print(f'Min: {minimum}, Max: {maximum}')
print(f'Average: {average}, Median: {median}, Count {count}')


# namedtuple方法
def get_stats_t(numbers):
    """
    计算最小值，最大值，列表数值的数量，平均数，中位数
    :param numbers: 一个纯数字的列表
    :return: 返回一个具名元祖res_stats
    """
    minimum = min(numbers)
    maximum = max(numbers)
    count = len(numbers)
    average = sum(numbers) / count

    sorted_numbers = sorted(numbers)
    middle = count // 2    # 双斜杠整除，向下取整
    if count % 2 == 0:     # 计算中位数算法
        lower = sorted_numbers[middle - 1]
        upper = sorted_numbers[middle]
        median = (lower + upper) / 2
    else:
        median = sorted_numbers[middle]
    stats = namedtuple('stats', 'minimum, maximum, average, median, count')
    res_stats = stats(minimum, maximum, average, median, count)
    return res_stats


a = get_stats_t(lengths)
print(a)
print(f'Min: {a.minimum}, Max: {a.maximum}')
print(f'Average: {a.average}, Median: {a.median}, Count {a.count}')
