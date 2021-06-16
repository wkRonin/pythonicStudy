import os


def sort_by_value(dd):
    """
    按字典的value排序
    """
    print(dict(sorted(dd.items(), key=lambda item: item[1])))


"""
题目：一个都是字符串的列表，返回最长公共前缀
"""


# 降序排列后的第一个字符串与最后一个字符串
def commonPrefixUtil(str1, str2):
    n1 = len(str1)
    n2 = len(str2)
    # 初始化字符串的索引与结果字符串
    result = ""
    j = 0
    i = 0
    while i <= n1 - 1 and j <= n2 - 1:
        if str1[i] != str2[j]:
            break
        result += (str1[i])
        i += 1
        j += 1
    return result


# A Function that returns the longest
# common prefix from the array of strings
def commonPrefix(arr_name, arr_length):
    """
    :param arr_name: 都是字符串的列表
    :param arr_length: 元素个数
    """
    # 降序排列
    arr_name.sort(reverse=False)
    # 传入commonPrefixUtil这个函数降序排列后的第一个字符串与最后一个字符串
    print(commonPrefixUtil(arr_name[0], arr_name[arr_length - 1]))


if __name__ == '__main__':
    ex_dict = {
        "A": 10,
        "B": 11,
        "C": 8
    }
    arr = ["geeksforgeeks",
           "geeks",
           "geek",
           "geezer"]
    n = len(arr)

    commonPrefix(arr, n)

    # 最直接的办法用自带库commonprefix
    print(os.path.commonprefix(arr))
