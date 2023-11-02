class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        left, mid , right = 0,0,len(nums) -1

        while mid <= right:
            if nums[mid] == 0:  #中间是0 就把0 干到左边
                nums[left],nums[mid] = nums[mid],nums[left]
                left += 1
                mid += 1

            elif nums[mid] == 2:#中间是2 就把2 干到右边
                nums[mid],nums[right] = nums[right],nums[mid]
                right -= 1
            else:
                mid += 1
        