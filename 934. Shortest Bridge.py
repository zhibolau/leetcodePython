class Solution(object):
    def shortestBridge(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n, queue, flag, d, result = len(grid), deque(), False, [(-1, 0), (1, 0), (0, -1), (0, 1)], -1
        
        def dfs(i, j): #找到是1的  然后都设置成2
            if not -1 < i < n or not -1 < j < n or not grid[i][j] or grid[i][j] == 2:
                return
            grid[i][j] = 2
            queue.append((i, j))
            for dx, dy in d:
                dfs(i + dx, j + dy)
                
        for i in range(n):
            if flag:
                break
            for j in range(n):
                if grid[i][j]:
                    dfs(i, j)
                    flag = True
                    break
        while queue:
            s = len(queue)
            result += 1
            for i in range(s):
                cur = queue.popleft()
                for dx, dy in d:
                    x, y = cur[0] + dx, cur[1] + dy
                    if not -1 < x < n or not -1 < y < n or grid[x][y] == 2:
                        continue
                    if grid[x][y] == 1:
                        return result
                    queue.append((x, y))
                    grid[x][y] = 2
        return result
    
"""DFS + BFS
先用 DFS 的方式找到第一座岛, 并将第一座岛加入队列
然后用 BFS 的方式搜索第一座岛到第二座岛的最短距离
可以将原岛屿值改成 2 标记访问过的位置
时间复杂度为 O(n ^ 2), 空间复杂度为 O(n ^ 2)


这道题说是有一个只有0和1的二维数组，其中连在一起的1表示岛屿，
现在假定给定的数组中一定有两个岛屿，问最少需要把多少个0变成1才能使得两个岛屿相连。
在 LeetCode 中关于岛屿的题目还不少，但是万变不离其宗，核心都是用 DFS 或者 BFS 来解，
有些还可以用联合查找 Union Find 来做。这里要求的是最小值，首先预定了一个 BFS，
这就相当于洪水扩散一样，一圈一圈的，用的就是 BFS 的层序遍历。好，现在确定了这点后，
再来想，这里并不是从某个点开始扩散，而是要从一个岛屿开始扩散
，那么这个岛屿的所有的点都是 BFS 的起点，都是要放入到 queue 中的，
所以要先来找出一个岛屿的所有点。找的方法就是遍历数组，找到第一个1的位置，
然后对其调用 DFS 或者 BFS 来找出所有相连的1，先来用 DFS 的方法，
对第一个为1的点调用递归函数，将所有相连的1都放入到一个队列 queue 中，
并且将该点的值改为2，然后使用 BFS 进行层序遍历，每遍历一层，结果 res 都增加1，
当遇到1时，直接返回 res 即可，
"""