class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        cur_sum = 0
        res = float('inf')
        for r in range(len(nums)): # 滑窗右边界扩张
            cur_sum += nums[r]
            while cur_sum >= target: # 满足条件  此时左边要一直动 看看有无更小的 
                res = min(res, r-left +1)
                cur_sum -=nums[left] # 滑窗左边界收缩   当前sum比target大 那当前的就不要了, 从sum中拿掉 并一定左光标
                left += 1
        return 0 if res ==  float('inf') else res


