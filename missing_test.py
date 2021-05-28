# -*- coding: utf-8 -*-
# @Time    : 2021/5/28 21:08
# @Author  : wkRonin
# @File    : missing_test.py
# @Software: PyCharm

# 如果要构造的默认值必须根据键名来确定，可自定义自己的dict子类并实现__missing__方法
# 文件路径path为key，文件句柄handle为value组成字典
path = 'account_9090.csv'
# 二进制模式写入
with open(path, 'wb') as f:
    f.write(b'asdsadsadasdd1111111')


# 辅助函数：二进制模式读写
def open_picture(profile_path):
    try:
        return open(profile_path, 'a+b')
    except OSError:
        print(f'Failed to open path {profile_path}')
        raise


class Pictures(dict):
    def __missing__(self, key):
        value = open_picture(key)
        self[key] = value
        return value


pictures = Pictures()
handle = pictures[path]
# handle1 = pictures['a.png']
handle.seek(0)  # 指针指向文件开头
image_data = handle.read()
print(pictures)
print(image_data)

