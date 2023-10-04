class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left,right = 0,len(nums)-1
        while left <right:
            mid  = (left+right)//2
            if nums[mid] <nums[mid+1]:
                left = mid+1
            else:
                right = mid
        return left
        
"""
有序数组，时间复杂度为 O(log n) 的算法，立马想到二分查找法。

数组的一半，一定是有序的，只要求出其中有序部分的最大值即可。比如【7,8,9,1,2,3,4,5】的右边一半【2,3,4,5】，
只要找出这部分的最大值就是正确的。再比如【6,7,8,9,1,2,3】的左边一半【6,7,8,9】，
找出此部分的最大值就是正确的。

"""