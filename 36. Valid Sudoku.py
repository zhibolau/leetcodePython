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