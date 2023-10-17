#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re

class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def str2tree(s):
    position = s.find('(')
    value = 0
    if position != -1:
        value = int(s[:position])
    else:
        value = int(s)
    cur = TreeNode(value)
    if position == -1:
        return cur
    count = 0
    start = position
    for i in range(start, len(s)):
        if s[i] == '(':
            count += 1
        elif s[i] == ')':
            count -= 1
        if count == 0 and start == position:
            cur.left = str2tree(s[start + 1:i])
            start = i + 1
        elif count == 0:
            cur.right = str2tree(s[start + 1: i])
    return cur

#请完成下面这个函数，实现题目要求的功能
#当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^ 
#******************************开始写代码******************************
# Remember to see the definition of the tree node above

def  findMax(root):
    if not root: 
        return float('-inf')
    res = root.val
    lres=findMax(root.left)
    rres=findMax(root.right)
    if lres> res: res = lres
    if rres>res: res= rres
    return res
    

#******************************结束写代码******************************


try:
    _treenode = str2tree(input())
except:
    _treenode = None

  
res = findMax(_treenode)

print(res)