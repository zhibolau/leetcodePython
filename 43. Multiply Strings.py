class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        len1,len2=len(num1),len(num2)

        d1=d2=0
        for i in range(len1):
            d1=d1*10+ord(num1[i])-ord('0')
        for i in range(len2):
            d2=d2*10+ord(num2[i])-ord('0')

        return str(d1*d2)