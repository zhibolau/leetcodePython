# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid):
        def dfs(grid, h, w, N):
            """
            用于构建方格([h, w], [h+N, w+N])的四叉树
            :param grid: 输入网格
            :param h: 方格左上角纵坐标
            :param w: 方格左上角横坐标
            :param N: 方格边长
            :return: 返回一棵构建好的四叉树
            """

            total = sum([grid[h+i][w+j] for i in range(N) for j in range(N)])   # 求取当前方格内的和

            if total == 0:                                              # 如果方格内所有元素都是0
                return Node(False, True, None, None, None, None)        # 构造一个值为False的叶子节点

            elif total == N * N:                                        # 如果方格内所有元素都是1
                return Node(True, True, None, None, None, None)         # 构造一个值为True的叶子节点

            else:                                                       # 说明方格内有0有1
                root = Node('*', False, None, None, None, None)         # 构造一个值为"*"的中间结点
                n = N // 2                                              # 求方格的一半
                root.topLeft = dfs(grid, h, w, n)                       # 构建左上子树
                root.topRight = dfs(grid, h, w+n, n)                    # 构建右上子树
                root.bottomLeft = dfs(grid, h+n, w, n)                  # 构建左下子树
                root.bottomRight = dfs(grid, h+n, w+n, n)               # 构建右下子树
                return root                                             # 返回构建完成的树

        return dfs(grid, 0, 0, len(grid))


if __name__ == "__main__":
    s = Solution()
    print(s.construct([[1, 1, 1, 1, 0, 0, 0, 0],
                       [1, 1, 1, 1, 0, 0, 0, 0],
                       [1, 1, 1, 1, 1, 1, 1, 1],
                       [1, 1, 1, 1, 1, 1, 1, 1],
                       [1, 1, 1, 1, 0, 0, 0, 0],
                       [1, 1, 1, 1, 0, 0, 0, 0],
                       [1, 1, 1, 1, 0, 0, 0, 0],
                       [1, 1, 1, 1, 0, 0, 0, 0],
                       ]))