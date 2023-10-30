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
    

#method 2
class Solution:
    # @param s : A string
    # @return : A string
    def reverseWords(self, s):
        #strip()去掉s头尾的空格，split()按照空格分割字符串，reversed翻转，''.join按照空格连接字符串
        return ' '.join(reversed(s.strip().split()))