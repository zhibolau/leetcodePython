class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        cur_sum = 0
        res = float('inf')
        for r in range(len(nums)): # 滑窗右边界扩张
            cur_sum += nums[r]
            while cur_sum >= target: # 满足条件
                res = min(res, r-left +1)
                cur_sum -=nums[left] # 滑窗左边界收缩
                left += 1
        return 0 if res ==  float('inf') else res


