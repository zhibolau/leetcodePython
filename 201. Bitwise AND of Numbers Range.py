class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while left < right:
            right = right & (right-1)
        return right
        

        """
        我们需要得到m,n所有元素按位与的结果。举个例子，当m=26，n=30时，它们的二进制表示为为： 11010　　11011　　11100　　11101　　11110 这个样例的答案是11000，易见我们发现我们只需要找到m和n最左边的公共部分即可。

在这题的解法中，我们将n与n-1按位与，当n的二进制为1010时，1010 & 1001 = 1000，相当于把二进制位的最后一个1去掉了。因此我们不断的做n^n-1的操作，直到n小于m相等即可。
        """