class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for index,interval in enumerate(intervals): 
            if interval[1] < newInterval[0]:#无交集
                res.append(interval)
            elif interval[0] > newInterval[1]: #此时把新的放入res最前面即可 因为新的比最小的还小，后面不用查看
                res.append(newInterval)
                return res+intervals[index:]
            else:#有交集
                newStart = min(interval[0],newInterval[0])
                newEnd = max(interval[1],newInterval[1])
                newInterval = [newStart,newEnd]
        res.append(newInterval)
        return res