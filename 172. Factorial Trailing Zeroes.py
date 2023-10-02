#尾随0的个数相当于因素5的个数

class Solution:
    def trailingZeroes(self, n: int) -> int:
        return 0 if n == 0 else n // 5 +self.trailingZeroes(n//5)