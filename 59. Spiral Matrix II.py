class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0]*n for _ in range(n)] #初始化n*n的matrix
        dire = [(0,1),(1,0),(0,-1),(-1,0)] #dir方向一定要这样 因为要顺时针！！！
        x,y,d = 0,0,0
        for i in range(1,n**2+1):
            res[x][y] = i #本来是0，访问过来就设置成1
            dx,dy=dire[d%4]
            if 0<= x+dx<n and 0<=y+dy<n and res[x+dx][y+dy] ==0:#在matrix范围内且未访问过
                x,y=x+dx,y+dy
            else:
                d +=1#否则换方向
                dx,dy=dire[d%4]
                x,y=x+dx,y+dy
        return res


"""首先初始化n*n的0矩阵, 然后定义向右, 向下, 向左, 向上的方向, 遍历n次, 每次将数字i 赋值给矩阵的某个位置, 
这里位置的确定条件是当下一个位置的index在矩阵范围之内并且下一个位置的值为0时, 我们按照当前方向走, 否则改变方向并更新x, y的值."""




#法2 newbi
class Solution(object):
    def generateMatrix(self, n):
        matrix = []
        start = n*n+1
        while start > 1:
        	# start=start - len(matrix),因为新增的row的列数一定等于之前的行数，
        	# 比如[[9][8]]两行，转过来新增的行肯定有两列，
        	# 新增行的结尾数是是之前的start-1，开始数和结尾数的差值是len(matrix)-1
        	#所以是range的时候，现在的end是之前的start，现在的start是之前start - len(matrix)
            start,end = start - len(matrix), start
            matrix = [range(start, end)] + zip(*matrix[::-1])
        return matrix       
#我的解法：先给9，然后每次把矩阵顺时针旋转，顶部push新一行，步骤如下：


