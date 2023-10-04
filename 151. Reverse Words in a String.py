class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        stack = []
        
        s_list = s.split()
        
        for i in s_list:
            stack.append(i)
        
        res = ""
        for i in range(len(stack)):
            res += stack.pop()+" "
        return res[:-1]