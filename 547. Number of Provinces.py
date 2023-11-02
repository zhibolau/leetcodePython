class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i):
            """以 i 为起点开始深度优先搜索
            """
            # 先进行标记
            visited[i] = 1
            # 继续搜索与 i 相连的城市
            for j in range(n):
                if isConnected[i][j] == 1 and not visited[j]:
                    dfs(j)


        # 城市数量
        n = len(isConnected)
        # visited 用以标记城市是否被访问
        visited = [0] * n
        # 用以存储省会的数量
        count = 0
        # 开始遍历城市进行搜索
        for i in range(n):
            # 城市未被访问时，开始搜索
            if not visited[i]:
                count += 1
                dfs(i)
        
        return count
            
