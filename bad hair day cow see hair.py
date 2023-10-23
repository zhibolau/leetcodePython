#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re

#请完成下面这个函数，实现题目要求的功能
#******************************开始写代码******************************

def  seeCows(cows):
    heights=cows
    heightStack = [] #stack里面放的都是比他矮的，  碰到高的就pop
    heightStack.append(len(heights))
    count = 0
    for i in range(len(heights) - 1, -1, -1):
        height = heights[i]
        while len(heightStack) > 1 and heights[heightStack[-1]] < height: #stack里面放的是index；
            heightStack.pop()
        count += heightStack[-1] - i - 1
        heightStack.append(i)
    return count
#https://www.cnblogs.com/Leohh/p/7636228.html
# 利用栈的后进的先出的特点进行操作，碰见比它大的就出栈，每次只需加上栈里元素的数量即可。

"""
The strategy to solve this problem is simple. At first we put all cows in line, 
then from right to left, we check each cow. At the same time we maintain a increasing 
stack that all items from top to bottom is increasing. Then we a cow comes, 
we first pop all records in the stack that is shorter than it, 
then we get from that cow's right to the top element of stack, 
all cows in this range is shorter than current one. 
We count the number and add current cow onto the stack at last."""

#******************************结束写代码******************************

arr = input()
cows = [int(item.group(0)) for item in re.finditer(r'-?\d+', arr)]
  
res = seeCows(cows)

print(res)