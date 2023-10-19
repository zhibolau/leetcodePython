class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0]+row, row+[0])]
            print(row)
        return row



a = Solution()
print(a.getRow(3))



class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        return self.generate(rowIndex+1)[rowIndex]
        
#LC 118
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res =[]
        for i in range(numRows):
            res.append([1])
            for j in range(1,i+1):
                if j == i:
                    res[i].append(1)
                else:
                    res[i].append(res[i-1][j-1] +res[i-1][j])
        return res