class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums) #否则超时
        now = 1
        for i in nums:
            if i > now:
                return now
            if i == now:
                now +=1
        return now
                
        