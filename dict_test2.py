'''
用get处理键不在字典中的情况，不使用in与KeyError
'''

counters = {
    'pumpernickel': 2,
    'sourdough': 1,
}
key = 'wheat'
# get方法，第一个参数指定自己想查的键，第二个参数指定这个键不存在时应返回的默认值。
count = counters.get(key, 0)
counters[key] = count + 1

print(counters)

# 每种面包的投票人为一个列表
votes = {
    'baguette': ['Bob', 'Alice'],
    'ciabatta': ['Coco', 'Deb'],
}

key = 'brioche'
who = 'Elmer'
if (names := votes.get(key)) is None:
    votes[key] = names = []

names.append(who)

print(votes)