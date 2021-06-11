'''
用defaultdict处理内部状态中缺失的元素，而不要用setdefault
'''


from collections import defaultdict


class Visits:
    def __init__(self):
        self.data = defaultdict(set)

    def add(self, country, city):
        # 访问这种字典的任意键时，总能得到一个已经存在的set实例，如果用setdefault，在字典里已经有这个键的情况还会毫无必要地分配一些set.
        self.data[country].add(city)


visits = Visits()
visits.add('England', 'Bath')
visits.add('England', 'London')
visits.add('China', 'Shanghai')
print(visits.data)
