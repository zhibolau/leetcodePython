class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        table = {}
        for i in nums:
            if i not in table:
                table[i] = 1
            else:
                table[i] += 1
        
        for key, value in table.items():
            if value > len(nums) / 3:
                res.append(key)

        return res