class Solution:
    """
    @param nums: An array of non-negative integers.
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber2(self, nums):
        if not nums:
            return 0
        n = len(nums)
        if n <= 3:
            return max(nums)
        ans1 = self.rob(nums[:n-1])
        ans2 = self.rob(nums[1:])
        return max(ans1, ans2)

    def rob(self, nums):
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[-1]
    
#算两次，第一次去掉第一座房子，第二次去掉最后一座房子，这样能避免第一座最后一座都被抢的情况。应该还比较简单易懂。

