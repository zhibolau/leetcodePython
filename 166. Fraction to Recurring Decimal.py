class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator % denominator == 0: #能整除
            return str(numerator // denominator)

        sign = "-" if numerator * denominator < 0 else "" #检查是否有负数
        num, den = abs(numerator), abs(denominator)

        n, rem = divmod(num, den)
        res = sign + str(n) + "." # 处理无限循环
        
        #纪录 rem 对应的位置
        num_to_pos = {}

        while rem and rem not in num_to_pos:
            num_to_pos[rem] = len(res) #加循环(的位置
            n, rem = divmod(10 * rem, den)
            res += str(n)

        if rem in num_to_pos:
            #如果rem重复，在对应的位置 插入 "("
            index = num_to_pos[rem]
            res = res[:index] + "(" + res[index:] + ")"

        return res
    
"""# returns the quotient and remainder of 8/3
result = divmod(8, 3)

print('Quotient and Remainder = ',result)

# Output: Quotient and Remainder =  (2, 2)
"""