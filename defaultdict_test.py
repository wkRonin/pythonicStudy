'''
用defaultdict处理内部状态中缺失的元素，而不要用setdefault
'''


from collections import defaultdict


class Visits:
    def __init__(self):
        self.data = defaultdict(set)

    def add(self, country, city):
        self.data[country].add(city)


visits = Visits()
visits.add('England', 'Bath')
visits.add('England', 'London')
visits.add('China', 'Shanghai')
print(visits.data)
