# -*- coding: utf-8 -*-
# @Time    : 2021/8/22 12:50
# @Author  : wkRonin
# @File    :ques0609.py
"""
已知一个由数字组成的列表，请将列表中的所有0移到右侧。
例如 move_zeros([1, 0, 1, 2, 0, 1, 3]) ，预期返回结果： [1, 1, 2, 1, 3, 0, 0]
"""
a = [1, 0, 1, 2, 0, 1, 3]

# 取巧法：key使用的是bool的方式排序，在Python中 0为False ，1为 True
assert sorted(a, reverse=True, key=bool) == [1, 1, 2, 1, 3, 0, 0]


# 解法1
class Solution1(object):
    def MoveZeros(self, nums):
        nums.append("&")
        while 0 in nums[:nums.index("&")]:
            nums.remove(0)
            nums.append(0)
        nums.remove("&")
        return nums


assert Solution1().MoveZeros(a) == [1, 1, 2, 1, 3, 0, 0]


# 解法2
class Solution2(object):
    def MoveZeros(self, nums):
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_item = nums.pop(i)
                nums.append(zero_item)
        return nums


assert Solution2().MoveZeros(a) == [1, 1, 2, 1, 3, 0, 0]


# 推导式解法
def move_zeros(li):
    return [x for x in li if x != 0] + [y for y in li if y == 0]


assert move_zeros(a) == [1, 1, 2, 1, 3, 0, 0]



