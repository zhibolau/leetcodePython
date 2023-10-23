#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re

#请完成下面这个函数，实现题目要求的功能
#******************************开始写代码******************************


def  isMaxHeap(nums):
    n = len(nums)
    for i in range(n):
      m = i * 2
      num = nums[i]
      if m + 1 < n: #2i+1 2i+2为根节点和2个孩子的index
         if num < nums[m + 1]:
            return False
      if m + 2 < n:
         if num < nums[m + 2]:
            return False
    return True


#******************************结束写代码******************************

arr = input()
nums = [int(item.group(0)) for item in re.finditer(r'-?\d+', arr)]

res = isMaxHeap(nums)

print('true' if res else 'false')
