
#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re

#请完成下面这个函数，实现题目要求的功能
#******************************开始写代码******************************


def  removeDuplicates(nums):
    if nums == []:
        return 0
    index = 0
    for i in range(1,len(nums)):
        if nums[i] != nums[index]:
            index +=1
            nums[index] = nums[i] #遇到过不一样的要更新成当前这个不一样的 因为后面可能还出现与当前不一样的的一样的 [1，1，2，2]
    return index+1


#method 2
    if not nums:
        return 0
    for i in range(len(nums)-1,0,-1):
        if nums[i] == nums[i-1]:
            nums.remove(nums[i])
    return len(nums)


#******************************结束写代码******************************

arr = input()
nums = [int(item.group(0)) for item in re.finditer(r'-?\d+', arr)]

res = removeDuplicates(nums)

print(res)