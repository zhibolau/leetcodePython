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
