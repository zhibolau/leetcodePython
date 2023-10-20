class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for i in range(len(triangle)-2,-1,-1):
            for j in range(0,i+1):
                triangle[i][j] +=min(triangle[i+1][j],triangle[i+1][j+1])
        return triangle[0][0]
