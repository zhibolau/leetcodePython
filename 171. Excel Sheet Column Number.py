class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        if not columnTitle:
            return 0
            
        res = 0
        for c in columnTitle:
            res = res * 26 + ord(c) - ord('A') + 1
        
        return res
    
#字符串转换成数字 26进制 把字符串转换为26进制数，注意是1-based

#考察的依然是高频考点：数位分离

