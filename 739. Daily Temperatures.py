class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures or len(temperatures) <2: return [0]
        n = len(temperatures)
        stack = []
        res = [0 for _ in range(n)]

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                res[stack[-1]]=i-stack[-1]
                stack.pop()
            stack.append(i)

        return res

        
