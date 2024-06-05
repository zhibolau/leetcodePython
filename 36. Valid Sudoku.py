class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        check = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] !='.':
                    r = str(i) +'row-'+board[i][j]
                    c = str(j) +'col-'+board[i][j]
                    board_idx = i //3 * 3+j//3 #第几个box 3x3的矩阵可以用i/3*3 + j/3来表示
                    box = str(board_idx) +'box-'+board[i][j]
                    if c in check or r in check or box in check:
                        return False
                    check.add(r)
                    check.add(c)
                    check.add(box)

        return True
    



            每个box里面9个格的index
    i=0 j=0 0  
    i=0 j=1 1
    i=0 j=2 2

    i=0 j=3 0
    i=0 j=4 1
    i=0 j=5 2
    
    i=0 j=6 0
    i=0 j=7 1
    i=0 j=8 2

    i=1 j=0 3 
    i=1 j=1 4
    i=1 j=2 5

    i=1 j=3 3
    i=1 j=4 4
    i=1 j=5 5
    
    i=1 j=6 3
    i=1 j=7 4
    i=1 j=8 5

    i=2 j=0 6 
    i=2 j=1 7
    i=2 j=2 8

    i=2 j=3 6
    i=2 j=4 7
    i=2 j=5 8
    
    i=2 j=6 6
    i=2 j=7 7
    i=2 j=8 8