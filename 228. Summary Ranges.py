class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        start = 0
        res = []
        for end in range(len(nums)):
            if end+1<len(nums) and nums[end+1] == nums[end]+1:
                continue
            if start !=end:
                res.append(str(nums[start])+'->'+str(nums[end]))
            else:
                res.append(str(nums[start]))
            start = end+1
        return res

