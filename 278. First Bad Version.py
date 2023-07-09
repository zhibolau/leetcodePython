# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        while left < right:
            mid = (left+right)//2
            if isBadVersion(mid): #这时候r是bad，再一次循环m在l与r中间，此时m不是bad， 再加一个就是第一个bad
                right= mid
            else:
                left = mid +1
        return left
            