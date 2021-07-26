# -*- coding: utf-8 -*-
# @Time    : 2021/7/26 22:22
# @Author  : wkRonin
# @File    :item_25.py
def safe_division(numeator, denominator, /,   # / 左边的参数只能以位置入参
                  nigits=10, *,               # 正常的关键字参数可以任意方式入参或不入
                  ignore_overflow=False,      # * 右边的参数只能以关键字入参或不入
                  ignore_zero_division=False):
    """
    计算两数相除的结果
    除数为0时抛出ZeroDivisionError异常，或返回无穷
    结果溢出时，抛出OverFlowError异常，或返回0
    :param numeator: 被除数
    :param denominator: 除数
    :param nigits: 保留小数位数
    :param ignore_overflow: 是否允许结果溢出
    :param ignore_zero_division: 是否允许除数为0
    :return: 计算结果
    """
    try:
        fraction = numeator / denominator
        return round(fraction, nigits)
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise


result = safe_division(12345666645545645688946465645456456465456465656546565654564564564566545645645645645645645645646456456456456654645456564564566666666666666666666666666666666666666688888888888886666666888888888888888888888888888666666688888888888888888888888888866666668888888888888888888888888886666666888888888888888888888888888666666688888888888888888888888888866666668888888888888888888888888886666666888888888888888888888888888666666688888888888888888888888888866666668888888888888888888888888886666666888888888888888888888888888666666688888888888888888888888888866666668888888888888888888888888886666666888888888888888888888888888666666688888888888888888888888888866666668888888888888888888888888886666666888888888888888888888888888666666688888888888888888888888888866666668888888888888888888888888886666666888888888888888888888888888666666688888888888888888888888888866666668888888888888888888888888886666666888888888888888888888888888666666688888888888888888888888888866666668888888888888888888888888886666666888888888888888888888888888666666688888888888888888888888888866666668888888888888888888888888886666666888888888888888888888888888666666688888888888888888888888888866666668888888888888888888888888886666666888888888888888888888888888666666688888888888888888888888888866666668888888888888888888888888886666666888888888888888888888888888666666688888888888888888888888888866666668888888888888888888888888886666666888888888888888888888888888666666688888888888888888888888888866666668888888888888888888888888886666666888888888888888888888888888666666688888888888888888888888888866666668888888888888888888888888886666666888888888888888888888888888666666688888888888888888888888888866666668888888888888888888888888886666666888888888888888888888888888666666688888888888888888888888888866666668888888888888888888888888886666666888888888888888888888888888666666688888888888888888888888888866666668888888888888888888888888886666666888888888888888888888888888666666688888888888888888888888888866666668888888888888888888888888886666666888888888888888888888888888666666688888888888888888888888888866666668888888888888888888888888886666666888888888888888888888888888666666688888888888888888888888888866666668888888888888888888888888886666666888888888888888888888888888666666688888888888888888888888888866666668888888888888888888888888886666666888888888888888888888888888666666688888888888888888888888888866666668888888888888888888888888886666666888888888888888888888888888666666688888888888888888888888888866666668888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888886666666666666666666666666666666666666666666666666666666666666666666669816533,
                       3, ignore_overflow=True)
print(result)
result1 = safe_division(1, 0, ignore_zero_division=True)
print(result1)
result2 = safe_division(1, 3, nigits=3)
print(result2)