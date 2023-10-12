class Solution:
    """
    @param word1: A string
    @param word2: A string
    @return: The minimum number of steps.
    """
    def minDistance(self, word1, word2):
        return self.helper(word1, len(word1), word2, len(word2), {})
        
    # cost when first i chars in w1 matchs first j chars in w2
    def helper(self, w1, i, w2, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if i == 0:
            return j
        
        if j == 0:
            return i
        
        cost = math.inf
        if w1[i - 1] == w2[j - 1]:
            cost = min(cost, self.helper(w1, i - 1, w2, j - 1, memo))
        else:
            # replace
            cost = min(cost, 1 + self.helper(w1, i - 1, w2, j - 1, memo))
            # remove
            cost = min(cost, 1 + self.helper(w1, i - 1, w2, j, memo))
            # insert
            cost = min(cost, 1 + self.helper(w1, i, w2, j - 1, memo))
        
        memo[(i, j)] = cost
        return cost
    """
    记忆化搜索。 dpi 表示把word1的前i位转化为word2的前j位所需要的最小代价。

str1转化为str2的min操作
    

给word1插入一个和word2最后的字母相同的字母，这时word1和word2的最后一个字母就一样了，
此时编辑距离等于1（插入操作） + 插入前的word1到word2去掉最后一个字母后的编辑距离
f[i][j - 1] + 1

删除word1的最后一个字母，此时编辑距离等于1（删除操作） + word1去掉最后一个字母到word2的
编辑距离 f[i - 1][j] + 1

把word1的最后一个字母替换成word2的最后一个字母，此时编辑距离等于 1（替换操作） +
 word1和word2去掉最后一个字母的编辑距离。为f[i - 1][j - 1] + 1
    """