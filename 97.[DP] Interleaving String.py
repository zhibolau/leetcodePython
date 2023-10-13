
#最好理解 但超时！！！！！！！！！
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        if len(s1) == 0:
            return s2 == s3
        if len(s2) == 0:
            return s1 == s3

        ans1 = False
        ans2 = False
        if s1[0] == s3[0]:
            ans1 = self.isInterleave(s1[1:], s2, s3[1:])
            
        if s2[0] == s3[0]:
            ans2 = self.isInterleave(s1, s2[1:], s3[1:])
            
        return ans1 or ans2
#好理解  递归
#s3的第一个char或者是s1的第一个char，或者是s2的，然后递归一下就可以了。


#非常不好写！！！！！！！！！！！！！！
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False

        dp = [None] * (len(s2) + 1)  # 初始化dp

        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if i == 0 and j == 0:
                    dp[j] = True
                elif i == 0:  # 计算上边界
                    dp[j] = dp[j-1] and s2[j-1] == s3[i+j-1]
                elif j == 0:  # 计算下边界
                    dp[j] = dp[j] and s1[i-1] == s3[i+j-1]
                else:  # 从两个方向向左下角计算
                    dp[j] = (dp[j] and s1[i-1] == s3[i+j-1]) or (dp[j-1] and s2[j-1] == s3[i+j-1])
        return dp[-1]
        
    
# s3 可否用s1 s2组合成
