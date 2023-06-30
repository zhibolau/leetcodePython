class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left = 0
        lookup = {}
        result = []

        for i in p:
            if i in lookup:
                lookup[i] += 1
            else:
                lookup[i] = 1
        
        for right,val in enumerate(s):
            if val in lookup:
                lookup[val] -= 1
            else:
                lookup[val] = -1
            
            while lookup[val] < 0:
                lookup[s[left]] += 1
                left += 1
            if right-left+1 == len(p):
                result.append(left)
        return result