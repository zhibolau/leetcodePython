class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum, res = 0 , -sys.maxsize
        for i in nums:
            sum += i
            res = max(sum,res)
            sum = max(0,sum)
        return res
        