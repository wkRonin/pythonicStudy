# -*- coding: utf-8 -*-
# @Time    : 2021/10/29 23:04
# @Author  : wkRonin
# @File    :item_37.py
"""
用组合起来的类来实现多层结构，不要用嵌套的内置类型
"""
from collections import namedtuple, defaultdict


class Subject:
    def __init__(self):
        self._grades = []

    def report_grade(self, score, weight):
        Grade = namedtuple('Grade', ('score', 'weight'))
        self._grades.append(Grade(score, weight))

    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight


class Student:
    def __init__(self):
        self._subjects = defaultdict(Subject)

    def get_subject(self, name):
        return self._subjects[name]

    def average_grade(self):
        total, count = 0, 0
        for subject in self._subjects.values():
            total += subject.average_grade()
            count += 1
        return total / count


class Gradesbook:
    def __init__(self):
        self._students = defaultdict(Student)

    def get_student(self, name):
        return self._students[name]


book = Gradesbook()
albert = book.get_student('Albert')
math = albert.get_subject('Math')
math.report_grade(75, 0.05)
math.report_grade(65, 0.15)
math.report_grade(70, 0.80)
gym = albert.get_subject('Gym')
gym.report_grade(100, 0.40)
gym.report_grade(80, 0.60)
print(albert.average_grade())


