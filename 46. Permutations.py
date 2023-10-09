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
    
#找到所有数组元素的组合


#dfs法
class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        output = []
        self.dfs(nums, [], output)
        return output
    
    def dfs(self, nums, workingSet, output):
        if len(nums) == len(workingSet):
            output.append(list(workingSet))
            return
        
        for num in nums:
            if num not in workingSet:
                workingSet.append(num)
                self.dfs(nums, workingSet, output)
                workingSet.pop()