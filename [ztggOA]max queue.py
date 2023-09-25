#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re
import math


    #请完成下面这个函数，实现题目要求的功能
    #当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
    #******************************开始写代码******************************#
class MyQueue:

    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.insert(0,x)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def max(self):
        return max(self.items)

    def empty(self):
        return self.items == []

#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** 结束写代码 ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** #

dsa_cnt = int(input())
dsa = []
for x in range(dsa_cnt):
    dsa.append(int(input()))

s = MyQueue()
for dsa_i in dsa:
    s.push(dsa_i)
    print(s.max(), " ")
    if s.empty():
        print("true", " ")
    else:
        print("false", " ")

for dsa_i in dsa:
    print(s.max(), " ")
    s.pop()
    if s.empty():
        print("true", " ")
    else:
        print("false", " ")