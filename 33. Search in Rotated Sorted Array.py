class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) -1
        while left <= right:
            mid = (left +right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left]: #若mid左边是排好序的
                if  nums[left]<= target < nums[mid]:
                    right = mid -1
                else:
                    left = mid + 1
            else:#若mid右边是排好序的
                if nums[mid]  < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1