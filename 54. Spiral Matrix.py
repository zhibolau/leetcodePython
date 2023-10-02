DIRECTIONS = [(0,-1),(0,1),(-1,0),(1,0)]
#python2会出错。。。。。。。。。
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]: return None
        q = deque()
        q.append((0,0,0))
        visited = set()
        visited.add((0,0))
        res = []
        while q:
            idx,x,y = q.popleft() #idx是方向的index 来选择 DIRECTIONS
            res.append(matrix[x][y])
            for i in range(4):
                delta_x,delta_y = DIRECTIONS[(idx+i)%4]
                new_x,new_y= x+delta_x,y+delta_y
                if self.valid(new_x,new_y,matrix,visited):
                    visited.add((new_x,new_y))
                    q.append(((idx+i)%4,new_x,new_y))
                    break
        return res

    def valid(self,x,y,matrix,visited):
        r = len(matrix)
        c = len(matrix[0])
        if  not(0<= x < r and 0<= y < c):
            return False
        if (x,y) in visited:
            return False
        return True


        