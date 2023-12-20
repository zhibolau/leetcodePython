class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum=0
        res=-sys.maxsize
        for i in nums:
            cur_sum +=i
            res=max(res,cur_sum)
            cur_sum=max(0,cur_sum)

        return res

#同时更新sum与0的最大值