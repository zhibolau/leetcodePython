class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """
    def numDecodings(self, s):
        # write your code here
        if not s or s[0] == '0': return 0
        dp, pointer = [1] * 3, 0
        for i in range(1, len(s)):
            pointer = i % 3
            dp[pointer] = 0
            if s[i] != '0': dp[pointer] += dp[pointer - 1]
            if 10 <= int(s[i - 1] + s[i]) <= 26:  #得先写s[i - 1]， 否则失败
                dp[pointer] += dp[pointer - 2]
        return dp[pointer]
#3位数组滚动处理DP。 注意遇到前导0可以直接判断为不可行。

