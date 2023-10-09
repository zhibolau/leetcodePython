class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        res = []
        temp = []
        self.dfs(n,k,1,0,temp,res) #chosen from the range [1, n]题要求从1开始
        return res
    
    def dfs(self,n,k,start,count,temp,res):
        if k == count:
            res.append(temp)
            return
        for i in range(start,n+1):
            self.dfs(n,k,i+1,count+1,temp+[i],res)
        
#找到给定个数的组合
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if not n or not k: return None
        return self.help(n,k,1,0,[],[])

    def help(self,n,k,start,count,res,tmp):
        if k==count:
            res.append(tmp)
            return res
        for i in range(start,n+1):
            self.help(n,k,i+1,count+1,res,tmp+[i]) #i+1开始就是不能本身比如 1，1 2，2
        return res

        