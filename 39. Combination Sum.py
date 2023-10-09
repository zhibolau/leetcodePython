class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        res = []
        self.dfs(candidates,target,0,[],res)
        return res

    def dfs(self,candidates,target,start,combinations,res):
        if target == 0:
            res.append(list(combinations))
            return res
        for i in range(start,len(candidates)):
            if candidates[i] > target:
                return
            combinations.append(candidates[i])
            self.dfs(candidates,target-candidates[i],i,combinations,res)
            combinations.pop()


#找target的组合，target变0 和 备选比target大 就结束