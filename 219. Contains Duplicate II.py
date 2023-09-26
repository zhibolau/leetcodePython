class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for index, val in enumerate(nums):
            if val in d and index - d[val] <=k:
                return True
            d[val] = index 
        return False
