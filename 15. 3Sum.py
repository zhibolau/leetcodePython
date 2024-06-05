class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]: #skip重复
                continue
            target = -nums[i]
            left= i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[left] + nums[right]
                if target == total:
                    res.append([nums[i] , nums[left] , nums[right]])

                    left += 1
                    while left < right and nums[left] == nums[left - 1]: #drop重复 上面l+1了所以查看l-1是不是与l重复了
                        left += 1
                    while left<right and nums[right] == nums[right - 1]:
                        right -= 1
                elif total > target:
                    right -=1
                else:
                    left +=1
        return res
                    
# 时间复杂度为O(n^2)，空间复杂度为O(1)