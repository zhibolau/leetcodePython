class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        resultCodeList = []
        for i in range(0,2 ** n):
            print("i: ")
            print(i)
            print("i>>1: ")
            print(i>>1)
            grayCode = (i >> 1)^i # ^是异或
            print("grayCode: ")
            print(grayCode)
            print("---------")
            resultCodeList.append(grayCode)
        return resultCodeList
    

"""如果a、b两个值不相同，则异或结果为1。如果a、b两个值相同，异或结果为0。
在python中用^表示，如下代码（注意是二进制表示）。

1 ^ 0 #结果为1，因为1和0不同

0 ^ 1 #结果为1，因为0和1不同

1 ^ 1 #结果为0，因为1和1相同

0 ^ 0 #结果为0，因为0和0相同"""

a=Solution()
print(a.grayCode(2))