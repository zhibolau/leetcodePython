

"""
使用动态规划：n=0时，为空树，那么dp[0]=1; n=1时，显然也是1，dp[1]=1；n=2时，dp[2]=2; 
对于n>2时，dp[n]=dp[0]dp[n-1]+dp[1]dp[n-2]+......+dp[n-1]*dp[0]
"""


class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        G = [0]*(n+1)
        G[0], G[1] = 1, 1

        for i in range(2, n+1):
            for j in range(1, i+1):
                G[i] += G[j-1] * G[i-j] # 在i点为root，左子序列构成左子树的数量为G[j-1]， 右面为G[i-j]

        return G[n]
    

"""一棵树由根节点，左子树和右子树构成。 对于目标n，根节点可以是1, 2, ..., n中的任意一个，
假设根节点为k，那么左子树的可能性就是numTrees(k-1)种，右子树的可能性就是numTrees(n-k)种，
他们的乘积就根节点为k时整个树的可能性。把所有k的可能性累加就是最终结果。"""
#法2 比较好理解

class Solution:
    # @paramn n: An integer
    # @return: An integer
    def numTrees(self, n):
        ans = {0: 1,
               1: 1,
               2: 2}
        return self.helper(n, ans)
    
    def helper(self, n, ans):
        if n in ans:
            return ans[n]
        else:
            # for each root node, there are 
            # (numTrees(left_subtree)) * (numTrees(right_subtree)) unique BST's
            res = 0
            for i in range(n):
                res += self.helper(i, ans) * self.helper(n - i - 1, ans)
            ans[n] = res
            return res
        
#算出有几个 ，  II 95题 是都有啥返回结果