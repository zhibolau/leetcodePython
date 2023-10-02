DIRECTION=[(0,1),(1,0),(1,1),(-1,-1),(-1,0),(0,-1),(1,-1),(-1,1)]
class Solution:
    """
    @param board: the given board
    @return: nothing
    """
    def gameOfLife(self, board):
        # Write your code here
        n=len(board)
        m=len(board[0])
        for i in range(n):
            for j in range(m):
                cntLive=0
                for moveX,moveY in DIRECTION:
                    newX,newY=i+moveX,j+moveY
                    if 0<=newX<n and 0<=newY<m and board[newX][newY]>0:
                        #挪动之后 是1 的话  cntLive为当前cell周边的存活数
                        cntLive+=1

                if board[i][j]>0: #live cell
                    if cntLive>3 or cntLive<2:
                        #Any live cell with more than three live neighbors dies
                        #Any live cell with fewer than two live neighbors dies
                        board[i][j]=2 #marked for dies later
                else:#dead cell
                    #Any dead cell with exactly three live neighbors becomes a live cell
                    if cntLive==3:
                        board[i][j]=-1 #becomes lives mark
        for i in range(n):
            for j in range(m):
                if board[i][j]==2:
                    board[i][j]=0 #Any live cell with fewer than two live neighbors dies
                if board[i][j]==-1: # becomes a live cell
                    board[i][j]=1
        return board