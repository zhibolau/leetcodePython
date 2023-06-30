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
            
            while lookup[val] < 0: #p出现s中没有的字母
                lookup[s[left]] += 1
                left += 1 #因为发现不一样的字母出现了 挪动指针/窗口
            if right-left+1 == len(p):
                result.append(left)
        return result