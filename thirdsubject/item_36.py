# -*- coding: utf-8 -*-
# @Time    : 2021/10/28 22:19
# @Author  : wkRonin
# @File    :item_36.py

# Example 1
import itertools

# help(itertools)

# Example 2
from pprint import pprint

it = itertools.chain([1, 2, 3], [4, 5, 6])
print(list(it))


# Example 3
it = itertools.repeat('hello', 3)
print(list(it))


# Example 4
it = itertools.cycle([1, 2])
result = [next(it) for _ in range(10)]
print(result)


# Example 5
it1, it2, it3 = itertools.tee(['first', 'second'], 3)
print(list(it1))
print(list(it2))
print(list(it3))


# Example 6
keys = ['one', 'two', 'three']
values = [1, 2]

normal = list(zip(keys, values))
print('zip:        ', normal)

it = itertools.zip_longest(keys, values, fillvalue='nope')
longest = list(it)
print('zip_longest:', longest)


# Example 7
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

first_five = itertools.islice(values, 5)
print('First five: ', list(first_five))

middle_odds = itertools.islice(values, 2, 8, 2)
print('Middle odds:', list(middle_odds))


# Example 8
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
less_than_seven = lambda x: x < 7
it = itertools.takewhile(less_than_seven, values)
print(list(it))


# Example 9
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
less_than_seven = lambda x: x < 7
it = itertools.dropwhile(less_than_seven, values)
print(list(it))


# Example 10
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = lambda x: x % 2 == 0

filter_result = filter(evens, values)
print('Filter:      ', list(filter_result))

filter_false_result = itertools.filterfalse(evens, values)
print('Filter false:', list(filter_false_result))


# Example 11
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_reduce = itertools.accumulate(values)
print('Sum:   ', list(sum_reduce))


def sum_modulo_20(first, second):
    output = first + second
    return output % 20


modulo_reduce = itertools.accumulate(values, sum_modulo_20)
print('Modulo:', list(modulo_reduce))


# Example 12
single = itertools.product([1, 2], repeat=2)
print('Single:  ', list(single))

multiple = itertools.product([1, 2], ['a', 'b'])
print('Multiple:', list(multiple))


# Example 13 N个元素形成的每种有序排列方式，包括元素相同，顺序不同
it = itertools.permutations([1, 2, 3, 4], 2)
original_print = print
print = pprint
print(list(it))
print = original_print


# Example 14 N个元素形成的每种无序组合，元素不同，顺序相同，算作同一种组合
it = itertools.combinations([1, 2, 3, 4], 2)
print(list(it))


# Example 15 N个元素形成的每种无序组合，但允许元素相同
it = itertools.combinations_with_replacement([1, 2, 3, 4], 2)
original_print = print
print = pprint
print(list(it))
print = original_print

