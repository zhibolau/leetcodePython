class Solution:
    """
    @param A: an integer ratated sorted array and duplicates are allowed
    @param target: An integer
    @return: a boolean 
    """
    def search(self, A, target):
        # write your code here
        if not A:
            return False
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] > A[end]:
                if A[start] <= target <= A[mid]:
                    end = mid
                else:
                    start = mid
            elif A[mid] < A[end]:
                if A[mid] <= target <= A[end]:
                    start = mid
                else:
                    end = mid
            else:
                end -= 1

        return target in [A[start], A[end]]
    
#有重复元素
"""
仔细想了想，也参考了其他童鞋的解答，二分确实是可以的。只要先判断mid在斜坡上，不管斜坡中间有没有平路，还是可以找到左半和右半边的。如果开头或者结尾出现了平路，直接开头+1或者结尾-1, 重新计算mid即可。不影响时间复杂度。但是最坏情况，时间复杂度会是O(n), 就是一直走start + 1或者end - 1，就相当于for循环了。

"""