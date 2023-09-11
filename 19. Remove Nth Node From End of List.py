#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#请完成下面这个函数，实现题目要求的功能
#当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^ 
#******************************开始写代码******************************

def removeNthFromEnd(head, n):
    dummy = ListNode(-1)
    dummy.next = head
    slow , fast = dummy, head
    for _ in range(n): #slow少走了
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next

#******************************结束写代码******************************


_removeNthF_cnt = 0
_removeNthF_cnt = int(input())
_removeNthF_i=0
_removeNthF = []
while _removeNthF_i < _removeNthF_cnt:
    _removeNthF_item = int(input())
    _removeNthF.append(_removeNthF_item)
    _removeNthF_i+=1

def get_list(nums):
    if len(nums) == 0:
        return None
    res = ListNode(0)
    curr = res
    for val in nums:
        curr.next = ListNode(val)
        curr = curr.next
    return res.next
  
head = get_list(_removeNthF)
n = int(input())
res = removeNthFromEnd(head, n)

cnt = 0
while res:
    print(str(res.val))
    res = res.next
    cnt += 1

print(str(cnt) + "\n")