class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        if not heights or not heights[0]: return []
        m, n = len(heights), len(heights[0])
        p_visited = [[False] * n for _ in range(m)]
        a_visited = [[False] * n for _ in range(m)]
        for i in range(m):
            self.dfs(p_visited, heights, m, n, i, 0)
            self.dfs(a_visited, heights, m, n, i, n -1)
        for j in range(n):
            self.dfs(p_visited, heights, m, n, 0, j)
            self.dfs(a_visited, heights, m, n, m - 1, j)
        res = []
        for i in range(m):
            for j in range(n):
                if p_visited[i][j] and a_visited[i][j]:
                    res.append([i, j])
        return res
        
    def dfs(self, visited, matrix, m, n, i, j):
        visited[i][j] = True
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        for dire in directions:
            x, y = i + dire[0], j + dire[1]
            if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] or matrix[x][y] < matrix[i][j]:
                continue
            self.dfs(visited, matrix, m, n, x, y)

"""
直接DFS求解。一般来说DFS需要有固定的起点，但是对于这个题，四条边界的每个位置都算作起点。

使用两个二维数组，分别记录每个位置的点能不能到达太平洋和大西洋。然后对4条边界进行遍历，看这些以这些边为起点能不能所有的地方。注意了，因为是从边界向中间去寻找，所以，这个时候是新的点要比当前的点海拔高才行。

最坏情况下的时间复杂度是O((M+N)*MN)，空间复杂度是O(MN)。
"""