class Solution:
    """
    @param num: An integer
    @return: true if num is an ugly number or false
    """
    def isUgly(self, num: int) -> bool:
        # write your code here
        if not num or num <= 0:
            return False
        for i in [2, 3, 5]:
            while num % i == 0:
                num //= i
        return num == 1