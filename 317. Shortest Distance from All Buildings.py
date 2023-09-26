"""
根据题意来看，building数肯定是比空地数要少很多的，
所以可以反向从building出发找每块空地与这个building的距离，
然后对于每个building都做同样的事，将结果叠加找最小值
"""

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        def bfs(i,j):
            visited = [[False]*n for _ in range(m)]
            q = collections.deque()
            q.append((i,j,1)) #1 is distance
            dirs = [[0,1],[0,-1],[-1,0],[1,0]]
           
            while q:
                i,j,dis = q.popleft()
                for d in dirs:
                    x = i+d[0] #4个方向走
                    y = j+d[1]
                    if 0<=x<m and 0<=y<n and not visited[x][y] and grid[x][y]==0:
                        distance[x][y] += dis
                        reach_num[x][y] += 1
                        q.append((x,y,dis+1))
                        visited[x][y] = True
               
               
        m,n = len(grid),len(grid[0])
        distance = [[0]*n for _ in range(m)] # store shortest number of edges (distance) from distance[row][col] to buildings
        reach_num = [[0]*n for _ in range(m)]# store number of buildings which can be reached from build[row][col]
        building_num = 0
       
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: #找到building了
                    bfs(i,j)
                    building_num += 1
       
        min_dist = float('inf')
        for i in range(m):
            for j in range(n):
                #当前是空地  并且 可以到达building，找最短距离
                if grid[i][j]==0 and reach_num[i][j]==building_num:  
                    min_dist = min(min_dist,distance[i][j])
       
        return min_dist if min_dist!=float('inf') else -1 