class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<2:
            return x
        
        l,r = 1, x//2
        while l<=r:
            mid = l + (r-l)//2
            if mid > x / mid:
                r = mid -1
            else:
                l = mid +1
        return (l-1)
            
   #二分法思路，从左边和右边同时去找想要的值去做不断逼近  
   #    时间复杂度 O(log(N))， 空间复杂度 O(1)