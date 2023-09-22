class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        n = len(nums)
        end = 0 #current index stops position as not start it yet
        for i in range(n):
            if i <= end: 
                end = max(end, i + nums[i]) #i + nums[i] means from positon i, where i could go the most
                #看当前end值是否可以到达终点
                if end >= n - 1:
                    return True
            else:
        return False
        