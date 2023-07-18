class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for index,interval in enumerate(intervals):
            if interval[1] < newInterval[0]:
                res.append(interval)
            elif interval[0] > newInterval[1]:
                res.append(newInterval)
                return res+intervals[index:]
            else:
                newStart = min(interval[0],newInterval[0])
                newEnd = max(interval[1],newInterval[1])
                newInterval = [newStart,newEnd]
        res.append(newInterval)
        return res