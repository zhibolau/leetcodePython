# 和1206题一样，简单直接的单调栈的应用。

# 环形数组的一个遍历技巧是复制range。比如，数组长度是4，用itertools.chain 可以形成这样一个range：0,1,2,3,0,1,2

# 如此，不用复制原数组，也不用丑陋的写两个循环

#数组是环状的

from itertools import chain
class Solution:
    
    def nextGreaterElements(self, nums):
        
        stack, g_map = [], {}
        
        for i in chain(range(len(nums)), range((len(nums)-1))):
            
            while stack and nums[stack[-1]] < nums[i]:
                g_map[stack.pop()] = i 
                
            stack.append(i)
            
        return [-1 if i not in g_map else nums[g_map[i]] for i in range(len(nums))]

#VERIFIED chain 可以用 rang_list = range(len(nums))+range((len(nums)-1)) 替换

