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


#method2
"""
举例看数组可能存在的几种形态，看在这几种数组形态中上面的解决思路是否能够找到Peak Element：

第一种是降序数组，如[5,4,3,2,1]，Peak Element为 0；i = 0时即满足nums[i] > nums[i + 1],返回0。

第二种是升序数组，如[1,2,3,4,5]，Peak Element为 4；遍历到终点i = 4发现都不满足nums[i] > nums[i+1]，因此数组中最后一个元素为Peak Element，返回4。

第三种是Peak Element在数组中间任意位置，如[1,3,2,4,5], Peak Element为 1；遍历到i = 1时满足nums[i] > nums[i+1]，因此返回1。

从上面的例子中也可以看到这种解决思路是可行的。
"""
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(0,len(nums)-1):
            if(nums[i] > nums[i+1]):
                return i
        return len(nums)-1
