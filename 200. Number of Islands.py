class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        res = 0
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == '1':
                    self.bfs(grid,x,y) #找到周边都是1的区域；都找遍了 数量加1，再去找下一个不相邻的1
                    res += 1
        return res

    def bfs(self,grid,x,y):
        queue = deque([(x,y)])
        grid[x][y] == '0' # 设置成0 说明已经计算过他了，本来他是1
        while queue:
            x,y = queue.popleft()
            for delta_x,delta_y in [(1,0),(0,-1),(0,1),(-1,0)]:
                new_x = x + delta_x
                new_y = y+delta_y
                if not self.valid(grid,new_x,new_y):
                    continue #发现0说明到边界了
                queue.append((new_x,new_y))
                grid[new_x][new_y] = '0' # 设置成0 说明已经计算过他了，本来他是1


    def valid(self,grid,x,y):
        rows = len(grid)
        cols = len(grid[0])
        return x >= 0 and x < rows and y >= 0 and y < cols and grid[x][y] == '1'