class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]: #一直找到s出现与t一样的s再挪动
                i += 1
            j += 1 #因为不一样所以j要一直挪动 直到出现一样的，因为是从t中找与s一样的 t长
        if len(s) == i:
            return True
        else:
            False
        