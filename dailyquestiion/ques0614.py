"""
找出两个list的相同元素和不同元素
"""

a = [6, 1, 1, 2, 3]
b = [1, 4, 2, 4, 5]
# 方法1：
seta = set(a)
setb = set(b)
print(seta & setb)
print(seta ^ setb)

# 方法2
def find_diff_by_twolist(list1,list2):
    '''
    :param list1: 列表1
    :param list2: 列表2
    :return:
    '''
    from collections import Counter
    newli=list(set(list1)) + list(set(list2))
    count=Counter(newli)
    same, diff = [], []
    for i in count.keys():
        if(count.get(i)>=2):
            same.append(i)
        else:
            diff.append(i)
    print("same is {},diff is {}".format(same, diff))

find_diff_by_twolist(a, b)