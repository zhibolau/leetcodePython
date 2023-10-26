class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        result = []
        nums = [lower-1] + nums + [upper+1]
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > 1:
                lb, ub = nums[i-1]+1, nums[i]-1
                result.append([lb, ub])
        return result