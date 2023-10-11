class Solution(object):
    def divide(self, dividend, divisor):
        INT_MAX = 2**31-1
        if divisor == 0:
            return INT_MAX
        a, b = abs(dividend), abs(divisor)
        ans, shift = 0, 31
        while shift >= 0:
            if a >= b << shift: #让shift以指数级别的往下减，   b << shift== 2* b^shift
                a -= b << shift
                ans += 1 << shift
            shift -= 1
        if dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0:
            ans = - ans
        if ans > INT_MAX:
            return INT_MAX
        return ans
    


    """
    基本思路是利用减法, 看看被除数可以减去多少次除数.

使用倍增的思想优化, 可以将减法的次数优化到对数时间复杂度.

我们将除数左移一位(或者让它加上自己), 即得到了二倍的除数, 这时一次减法相当于减去了2个除数. 不断倍增, 时间效率很优秀.

与此同时还需要一个变量记录此时的除数是最初的除数的多少倍, 每次减法后都加到结果上即可

左移记住是乘  , 右移是除

a = 2
print(a << 3)  # 相当于a 乘 2的3次方

a = 32
print(a >> 3)  # 相当于a 除 2的3次方
    """