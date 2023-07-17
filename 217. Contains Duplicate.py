class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}

        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        for i in d.keys():
            if d[i] >=2:
                return True
        return False
        
    #method 2
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in nums:
            if i in d:
                return True
            d[i] = True
        return False