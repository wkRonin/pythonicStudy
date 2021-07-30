# -*- coding: utf-8 -*-
# @Time    : 2021/7/29 22:20
# @Author  : wkRonin
# @File    :item_29.py
"""
用赋值表达式消除推导中的重复代码
编写推导式与生成器表达式时，在描述条件的那一部分通过赋值表达式定义变量，并在其他部分复用该变量
"""
"""
判断库存是否满足订单，核查每种产品 有没有达到发货的最低限制
8个位一批，至少要有一批，才能发货
"""
stock = {
    'nails': 125,
    'screws': 35,
    'wingnuts': 8,
    'washers': 24,
}

order = ['screws', 'wingnuts', 'clips']


def get_batches(count, size):
    return count // size


result = {}
for name in order:
  count = stock.get(name, 0)
  batches = get_batches(count, 8)
  if batches:
    result[name] = batches

print(result)

# batches := get_batches(...)赋值表达式，能够从stock字典里查到对应产品一共有几批，并把这个批数放在batches变量里
found = {name: batches for name in order
         if (batches := get_batches(stock.get(name, 0), 8))}
assert found == {'screws': 4, 'wingnuts': 1}, found

# stock中 十个为一批能发货的
result = {name: tenth for name, count in stock.items()
          if (tenth := count // 10) > 0}
print(result)

# 迭代器
foundd = ((name, batches) for name in order
         if (batches := get_batches(stock.get(name, 0), 8)))
print(next(foundd))
print(next(foundd))