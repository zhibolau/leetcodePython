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

        
#method 2
    def champagneTower(self, poured, query_row, query_glass):
        # write your code here

        # f[i][j]: arrived champagne at (i,j)
        f = [[0 for j in range(query_row + 1)] for i in range(query_row + 1)]
        f[0][0] = poured

        for i in range(1, query_row + 1):
            f[i][0] = 0.5 * max(f[i - 1][0] - 1, 0)
            for j in range(1, min(i + 1, query_row + 1)):
                f1 = max(f[i - 1][j] - 1, 0)
                f2 = max(f[i - 1][j - 1] - 1, 0)
                f[i][j] = (f1 + f2) * 0.5

        return float(min(f[query_row][query_glass], 1))