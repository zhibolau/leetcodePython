class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        s = sorted(nums)
        self.dfs(result, [], s)
        return result
        
    def dfs(self, result, tmp, s):
        if not s:
            result.append(list(tmp))
            return
        for i in range(len(s)):
            if i > 0 and s[i] == s[i-1]: continue
            tmp.append(s[i])
            self.dfs(result, tmp, s[:i]+s[i+1:])
            tmp.pop()
        