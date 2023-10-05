class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lookup = {}
        for i in s:
            if i not in lookup:
                lookup[i] = 1
            else:
                lookup[i] += 1
            
        for j in t:
            if j not in s:
                return False
            else:
                lookup[j] -= 1
        
        for l in lookup:
            if lookup[l] != 0:
                return False
        
        return True