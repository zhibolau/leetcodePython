"""
算法思路： 
1. 二分第一列， 判断rowIndex 
2. 二分 matrix rowIndex , 
判断target是否在矩阵中

复杂度： log(m) + log(n)

容易混淆的点： 二分的时候， 根据矩阵的规律， target 比end还要大的时候，应该返回end。 因为此时end是目标行的第一个
"""

class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix:
            return False
    
        m, n = len(matrix), len(matrix[0])
        firstCol = [matrix[i][0] for i in range(m)]
        rowIndex = self.binarySearch(firstCol, target)
        colIndex = self.binarySearch(matrix[rowIndex], target)
        #print(rowIndex)
        if matrix[rowIndex][colIndex] == target:
            return True
        return False
        
    def binarySearch(self, nums, target):
        start, end = 0, len(nums)-1
        while start+1 < end:
            mid = (start+ end)//2
            if nums[mid] <= target:#注意等号
                start = mid
            else:
                end = mid
        
        if nums[end] <= target: #注意等号
            return end
        return start