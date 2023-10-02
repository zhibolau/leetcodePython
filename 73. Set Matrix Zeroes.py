class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]: return None
        row = len(matrix)
        col = len(matrix[0])
        row_bol = [False for i in range(row)]
        col_bol = [False for i in range(col)]
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:#根据0出现的位置找到 坐标值 
                    row_bol[i] = True
                    col_bol[j] = True

        for i in range(row):
            for j in range(col):
                if row_bol[i] or col_bol[j]:
                    matrix[i][j] = 0