class Solution:
    def isHappy(self, n: int) -> bool:
        d = {}
        while True:
            d[n] = 1
            n = sum(int(x) * int(x) for x in str(n))
            if n == 1 or n in d: # n再次出现在d 或者为1 就停了
                break
        return n == 1