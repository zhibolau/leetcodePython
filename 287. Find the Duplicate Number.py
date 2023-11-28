#O(n lgn)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        size = len(nums)

        left = 1
        right = size - 1

        while left < right:
            # 先找中间值
            mid = left + (right - left) // 2
            # mid = (left + right) // 2
            # 遍历数组
            # 统计数组中小于等于中间值的元素个数
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            
            # 如果统计数严格大于中间值时，那么重复值将落在 [left, mid] 这个区间
            if count > mid:
                # 将右边界缩小到 mid
                right = mid
            # 否则重复值落在 [mid + 1, right]
            else:
                left = mid + 1
        return left




#O(n)
class Solution:
    # @param {int[]} nums an array containing n + 1 integers which is between 1 and n
    # @return {int} the duplicate one
    def findDuplicate(self, nums):
        # Write your code here
        if len(nums) <= 1:
            return -1

        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = 0;
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
        
        return slow
    