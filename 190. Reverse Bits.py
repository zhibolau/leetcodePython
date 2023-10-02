class Solution:
    def reverseBits(self, n: int) -> int:
        # x << y == x * 2**y
        # x >> y == x / 2**y
        # a= 1 b = 2 a|b = 3   1 0 | 0 1 = 1 1
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31-i))

        return res