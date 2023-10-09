class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <=1:
            return [nums]
        
        res = []
        for i in range(len(nums)):
            num = nums[i]
            rest = self.permute(nums[:i]+nums[i+1:])
            for r in rest:
                res.append([num]+r)
                
        return res