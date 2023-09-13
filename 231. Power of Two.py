class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #method 1 32 位有符号整数的范围内，最大的2的幂为 2^30，
        # 只需判断其为正数且为2^30的约数即可。 O(1)
        return n > 0 and 2 ** 30 % n == 0

        # transfer to binary and =it should only contain 1 "1" (or 0 with 0 "1")
        # 2: 10 binary format
        # 4: 100
        # 8: 1000
        return str(bin(n)).count("1") <= 1 and n > 0


        