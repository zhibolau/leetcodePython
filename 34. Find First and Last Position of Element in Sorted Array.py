"""
做两遍二分搜索，如果不能找到target的话返回（-1，-1）如果能找到的话第一遍返回最小的index，
第二遍返回最大的index，这样的话可以保证在最差的情况下时间复杂度是O(log(n))。
"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums: return [-1,-1]
        return [self.b_s_first(nums,target),self.b_s_second(nums,target)]

    
    def b_s_first(self,nums,target):
        start,end = 0,len(nums)-1
        while start+1<end:
            mid= (start+end)//2
            if nums[mid]<target:#这里没有等于
                start=mid
            else:
                end =mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1

    def b_s_second(self,nums,target):
        start,end = 0,len(nums)-1
        while start+1<end:
            mid= (start+end)//2
            if nums[mid]<=target:   #这里有等于
                start=mid
            else:
                end =mid
        if nums[end] == target:
            return end
        if nums[start] == target:
            return start
        return -1
        
