class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res =[]
        for i in range(numRows):
            res.append([1]) #每次进来添加1，因为收尾都是1
            for j in range(1,i+1):
                if j == i:
                    res[i].append(1) #到尾了  就添加1
                else:
                    res[i].append(res[i-1][j-1] +res[i-1][j]) #其余时候加上一个的两个和
        return res