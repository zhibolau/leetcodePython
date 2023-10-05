#https://youtu.be/re-WQ14s-Kg?si=nHZSttvIQYUScn7N

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        res = [''] * numRows
        row = 0
        step = 1

        for i in s:
            res[row] += i
            if row ==0: #在到达numRows-1之前，row一直在递增
                step = 1
            elif row == numRows-1: #到底儿了 就开始递减到0
                step = -1
            row += step #step用来调整行数变化的
        return ''.join(res)
        