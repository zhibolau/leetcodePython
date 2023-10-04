class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start,end = 0,len(nums)-1
        while start<end:
            #1,2,3,4,5
            if nums[start]<nums[end]: return nums[start] # 说明数组没有翻转，还是升序情况 min在最左
            mid = (start+end)//2
            #nums[start] > nums[end]
            if nums[start]>nums[mid]: # 4，5，1，2，3 # start比mid大 说明mid右边为升序，mid肯定为右边的min，所以除了mid就不考虑右边了
                end = mid
            else: # 3，4，5，1，2 start 3比mid 5小，说明mid左边为升序，mid为左边最大值 同时start>end，所以min在右半段
                start = mid+1
        return nums[start]