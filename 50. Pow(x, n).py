class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return self.dfs(1/x, -n)
        else:
            return self.dfs(x, n)
    
    def dfs(self,x, n):
        if n == 1: #base case
            return x
        res = self.dfs(x, n //2)  # so below could use res * res based on n odd or even
        if n %2 == 0:
            return res * res
        else:
            return res * res * x
    