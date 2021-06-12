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
