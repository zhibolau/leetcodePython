class Solution:
    def intToRoman(self, num: int) -> str:
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        res = ''
        for i in range(len(nums)):
            while num >= nums[i]: #用while是因为3000的时候一直得用1000 所以要一直跟1000比  知道 低于1000了 才看下一个nums的元素
                num -= nums[i]
                res += romans[i]

        return res