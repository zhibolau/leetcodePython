class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = [] 
        while columnNumber > 0: 
          c = chr((columnNumber - 1) % 26 + ord('A'))  #找个位
          result.append(c) 
          columnNumber = (columnNumber - 1) // 26  #找10位
        return ''.join(result[::-1]) 
    

#26进制 每次除以26得到的余数对应相应位数的字母