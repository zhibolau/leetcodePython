"""
建立二维数组dp，令dp[i][j]表示到达 i, j的最多路径数。
初始化：对于第一行 dp[0][j]，或者第一列 dp[i][0]，都只有一条路径。
机器人到达位置(i, j)有两种方式：从(i - 1, j)下移和从(i, j - 1)右移。
状态转移方程为：
dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
"""

class Solution:

    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """

    def uniquePaths(self, m, n):
        dp = [[0] * n for _ in range(m)] #m为rows， 所以先【0】*n
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]