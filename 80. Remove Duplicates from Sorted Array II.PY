class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return n
        left = 2
        for right in range(2,n):
            if nums[left-2] != nums[right]:
                nums[left] = nums[right]
                left += 1
        return left
        