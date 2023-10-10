#经典的动态规划问题 状态转移方程 dpi = min(dpi-1 + costi-1,dpi-2 + costi-2)


class Solution:
    """
    @param cost: an array
    @return: minimum cost to reach the top of the floor
    状态转移方程 dp[i] = min(dp[i-1] + cost[i-1],dp[i-2] + cost[i-2])
    """
    def minCostClimbingStairs(self, cost):
        # Write your code here
        a, b = 0, 0
        for i in range(2, len(cost) + 1):
            c = min(a + cost[i - 2], b + cost[i - 1])
            a, b = b, c
        return b