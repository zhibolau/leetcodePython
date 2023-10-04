class Solution:
    #brute force TIME exceed
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        size = len(nums)
        if not nums:
            return res
        for i in range(size):
            product = 1
            for j in range(size):
                if i ==j:
                    continue
                else:
                    product *= nums[j]
            res.append(product)
        return res

# O N 1
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        res = [1] *size
        pre_p = post_p = 1
        # 将第 i 个位置乘上前 i - 1 个数的积
        for i in range(size):
            res[i] *= pre_p
            pre_p *= nums[i]
# 将第 i 个位置乘上后面数的积
        for i in range(size-1,-1,-1):
            res[i] *= post_p
            post_p *= nums[i]
        return res

"""
观察可以发现，每个数其实就是它前面部分的积乘以后面部分的积。所有前缀的积，通过一次遍历即可算出来，后缀也是一样。
我们可以边乘边算前缀积，同时将他乘在结果数组上，这样达到了O(1)的额外空间，同时不用到除法。

令result为一个全是1的数组。
令前缀积prefixProduct等于1，后缀积postfixProduct等于1。
正序遍历数组nums，第i个位置先将结果乘上prefixProduct，再将prefixProduct乘上nums[i]。
逆序遍历数组nums，第i个位置先将结果乘上postfixProduct，再将postfixProduct乘上nums[i]。
返回result。
"""