class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if not str:
            return ""
        
        for i in range(len(strs[0])):
            for string in strs[1:]:
                if i >= len(string) or string[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]
    


#法2

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        result =""
        
        i = 0
        
        while True:
            try:
                sets = set(string[i] for string in strs)
                if len(sets) ==1:
                    result += sets.pop()
                    i += 1
                else:
                    break
            except:
                break
                
        return result
                        