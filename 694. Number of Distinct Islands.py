class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        queue,check,ans = deque(),set(),0
        row, col = len(grid), len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    path = " "
                    queue.append((i,j))
                    grid[i][j] = 0
                    while queue:
                        x,y = queue.popleft()
                        for dx,dy in [(0,-1),(1,0),(0,1),(-1,0)]:
                            new_x = x+dx
                            new_y = y+dy
                            if self.is_valid(grid,new_x,new_y):

                                queue.append((new_x,new_y))
                                grid[new_x][new_y] = 0
                                path += str(new_x-i) + str(new_y-j)
                    if path not in check:
                        ans+=1
                        check.add(path)
        return ans



    
    def is_valid(self, grid, x, y):
        row, col = len(grid), len(grid[0])
        return x >= 0 and x < row and y >= 0 and y < col and grid[x][y] == 1
        