drill = (4, 'drill')
sander = (4, 'sander')
assert drill[0] == sander[0]
assert drill[1] < sander[1]
assert drill < sander


class Tool:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f'Tool({self.name!r}, {self.weight})'


power_tools = [
    Tool('a', 4),
    Tool('b', 5),
    Tool('c', 40),
    Tool('D', 4)
]
# 重量从小到大，字母从小到大
power_tools.sort(key=lambda x: (x.weight, x.name))
print(power_tools)
# 重量从大到小，字母从小到大方法一
power_tools.sort(key=lambda x: (-x.weight, x.name))
print(power_tools)
# 重量从大到小，字母从小到大方法二
power_tools.sort(key=lambda x: x.name)  # 字母为次要指标，默认升序
power_tools.sort(key=lambda x: x.weight,
                 reverse=True)          # 重量为主要指标，降序
print(power_tools)
# 重量从大到小，字母从大到小
power_tools.sort(key=lambda x: (x.weight, x.name),
                 reverse=True)
print(power_tools)
# 总结：若指标不支持一元减操作符，可以多次调用sort方法，最次要的指标放在第一轮处理，然后逐步处理更重要的指标，首要指标放在最后一轮处理
# 若字母有大小写，大写字母默认排在小写字母前面，用lower()方法变成小写后再排序
