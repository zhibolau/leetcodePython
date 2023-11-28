class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0

        return (num - 1) % 9 + 1
        


class Solution:
    """
    @param num: a non-negative integer
    @return: one digit
    """
    def addDigits(self, num):
        # write your code here
        if num <= 9:
            return num
        else:
            num = sum(int(n) for n in list(str(num)))
            return self.addDigits(num)