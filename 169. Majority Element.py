class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        check = len(nums)//2
        d = {}
        for i in nums:
            try:
                d[i] += 1
            except:
                d[i] = 1
            if d[i] >check:
                return i

"""
字典记录item出现次数
检查次数是否超过限制
"""