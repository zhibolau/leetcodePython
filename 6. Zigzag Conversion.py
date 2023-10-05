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
            if row ==0:
                step = 1
            elif row == numRows-1:
                step = -1
            row += step
        return ''.join(res)
        