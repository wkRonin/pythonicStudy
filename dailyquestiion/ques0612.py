"""
题目：给定一段英文文本（单词间都是空格分隔），请编写一个函数，将每个单词的首字母转成大写。

def to_capital(words):
    # your codes
示例：

输入："hogwarts school of witchcraft and wizardry"
输出："Hogwarts School Of Witchcraft And Wizardry"
"""


def To_Capital(words):
    """
    打印全部首字母大写
    :param words:输入的字符串
    :return:
    """
    print('全部首字母大写： ' + words.title())


hogwarts = 'hogwarts school of witchcraft and wizardry'
To_Capital(hogwarts)
print('所有字母大写: ' + hogwarts.upper())
print('所有字母小写: ' + hogwarts.lower())
print('首字母大写，其余都小写： ' + hogwarts.capitalize())
print('大写转小写，小写转大写： ' + hogwarts.swapcase())

# 数据转换题
test = [
    {'fQY': 'A', 'fWD_MC': 'a1'},
    {'fQY': 'A', 'fWD_MC': 'a2'},
    {'fQY': 'A', 'fWD_MC': 'a3'},
    {'fQY': 'B', 'fWD_MC': 'b1'},
    {'fQY': 'C', 'fWD_MC': 'c1'},
    {'fQY': 'C', 'fWD_MC': 'c2'}
]

# 预期结果：
# result= [
#     {'name': 'A', 'children': [{'name': 'a1'}, {'name': 'a2'}, {'name': 'a3'}]},
#     {'name': 'B', 'children': [{'name': 'b1'}]},
#     {'name': 'C', 'children': [{'name': 'c1'}, {'name': 'c2'}]}
# ]
res = []
for item in test:
    for data in res:
        if data['name'] == item['fQY']:
            data['children'].append({'name': item['fWD_MC']})
            break
    else:
        res.append({'name': item['fQY'], 'children': [{'name': item['fWD_MC']}]})
print(f'结果：{res}')


