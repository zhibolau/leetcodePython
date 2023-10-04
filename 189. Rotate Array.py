class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%(len(nums))
        nums[:k],nums[k:] = nums[len(nums)-k:],nums[:len(nums)-k]
"""
利用py的数组切片操作
"""