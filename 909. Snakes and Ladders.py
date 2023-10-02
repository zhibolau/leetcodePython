class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def get_rc(idx):
            r,c = (idx-1)//n, (idx-1) %n

            if r % 2 == 1:
                c = n - 1 - c
            return n-1-r, c

        q = deque()
        q.append((1,0))
        visited = set()
        while q:
            idx,step = q.popleft()
            for i in range(1,7):
                idx_next = idx + i
                if idx_next > n * n:
                    return -1
                
                new_x, new_y = get_rc(idx_next)
                if board[new_x][new_y] >0:
                    idx_next = board[new_x][new_y]
                if idx_next == n * n:
                    return step+1
                if idx_next not in visited:
                    visited.add(idx_next)
                    q.append((idx_next,step+1))
        return -1