class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        #brute force
#Time Limit Exceeded

        # max_v = 0
        # for i in range(len(height)):
        #     for j in range(len(height)):
        #         if max_v < abs(j-i) * min(height[j],height[i]):
        #             max_v = abs(j-i) * min(height[j],height[i])
        # return max_v

# 2 pointer
        max_v = 0
        l = 0
        r = len(height) -1
        while l != r:
            if height[l] > height[r]:
                max_v = max(max_v, height[r] * (r-l)) #要可矮的  要不然漏水了。。。
                r -= 1
            else:
                max_v = max(max_v, height[l] * (r-l))
                l += 1
        return max_v



