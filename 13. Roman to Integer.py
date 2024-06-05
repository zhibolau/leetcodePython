class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        d = {'I':1,'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for i in range(len(s)-1): # 因为下边要看i+1 所以这里面减1
            if d[s[i]]<d[s[i+1]]:
                res -=d[s[i]]
            else:
                res +=d[s[i]] #这里包括大于等于的情况 比如 III，所以顺序不能错
        return  res+d[s[-1]]
    

"""
模拟罗马数字运算 举个例子就懂
IV
"""