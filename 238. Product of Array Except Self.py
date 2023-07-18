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
