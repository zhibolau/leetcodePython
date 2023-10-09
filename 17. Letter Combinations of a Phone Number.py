class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) ==0:
            return None
        
        digit_letter ={
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        }
        
        res = [""]
        
        for i in digits:
            temp =[]
            for k in digit_letter[i]:
                for s in res:
                    temp.append(s+k)
            res =temp
            
        return res
    
#给定电话号，返回所有字母组合