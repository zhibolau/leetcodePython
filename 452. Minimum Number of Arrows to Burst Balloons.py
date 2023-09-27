class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        ans = 1
        points.sort(key=lambda x:x[1])
        last_end = points[0][1]
        for i in range(1,len(points)):
            if points[i][0] > last_end: #看下一个元素的起点是不是大于上一个的终点
                ans +=1
                last_end = points[i][1]
        return ans 
