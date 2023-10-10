class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not word:
            return False
        
        width = len(board[0])
        height = len(board)
        
        for x in range(height):
            for y in range(width):
                if self.dfs(board,word,x,y,height,width,0):
                    return True
        
        return False
    
    def dfs(self,board,word,x,y,height,width,count): #count为word的indx ，第一个字母不一样肯定就找不到这个word了
        if x <0 or x ==height or y <0 or y ==width or word[count] != board[x][y]:
            return False
        if len(word) -1 == count: #count为idx 最大为word长度-1
            return True
        cur = board[x][y]
        board[x][y] =0
        
        res= self.dfs(board,word,x+1,y,height,width,count+1) or self.dfs(board,word,x-1,y,height,width,count+1) or self.dfs(board,word,x,y+1,height,width,count+1) or self.dfs(board,word,x,y-1,height,width,count+1)
        board[x][y] = cur
        return res