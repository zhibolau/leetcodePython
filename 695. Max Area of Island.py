class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        width = len(grid)
        length = len(grid[0])
        max_area =0
        for i in range(width):
            for j in range(length):
                if grid[i][j] == 1:
                    max_area = max(max_area, self.dfs(grid,i,j,1))
        return max_area
    
    def dfs(self,grid, i,j,res):
        grid[i][j] = 0
        for m,n in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
            if (m>=0 and m<len(grid) and n>=0 and n<len(grid[0]) and grid[m][n] == 1):
                res =1+ self.dfs(grid,m,n,res) 
        return res

        