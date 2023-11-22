class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res =[]
        temp =[]
        self.dfs(nums,0,temp,res)
        
        return res
    
    def dfs(self,nums,start,temp,res):
        res.append(list(temp))
        
        for i in range(start,len(nums)):
            self.dfs(nums,i+1,temp+[nums[i]],res)
        