class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0: return []
        
        res =[]
        
        self.gen_p(n,n,'',res)
        
        return res
    
    def gen_p(self,left_paren_amount,right_paren_amount,item,res):
        if left_paren_amount > right_paren_amount:
            return
        if right_paren_amount == left_paren_amount == 0:
            res.append(item)
        if left_paren_amount >0:
            self.gen_p(left_paren_amount-1,right_paren_amount,item+'(',res)
        if right_paren_amount >0:
            self.gen_p(left_paren_amount,right_paren_amount-1,item+')',res)
#组合成n对括号 dfs