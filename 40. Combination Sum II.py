class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(list(candidates))
        res = []
        self.dfs(candidates,target,0,[],res)
        return res
        
    def dfs(self,candidates, target, start, combination, results):
        if target == 0:
            return results.append(list(combination))
            
        for i in range(start,len(candidates)):
            if target < candidates[i]:#由于已经排序了 这里大于的 后边肯定也都大于 所以break
                return
            if i > start and candidates[i] == candidates[i-1]:
                continue
            combination.append(candidates[i])
            self.dfs(candidates,target-candidates[i],i+1,combination,results)
            combination.pop()  #pop delete element at the end
