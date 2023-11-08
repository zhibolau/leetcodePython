class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s: return None

        return self.help(s,{})

    def help(self,s,memo):
        if not s: return [[]]
        if s in memo: return memo[s]
        res = []
        for i in range(len(s)):
            pre=s[:i+1]
            if pre==pre[::-1]: #一样的才是palin
                parts=self.help(s[i+1:],memo) #再找到i+1的palin 进行组合
                for i in parts:
                    res.append([pre]+i)
        memo[s] = res
        return res