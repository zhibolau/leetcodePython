class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        p = []
        for x in nums:
            heapq.heappush(p, x)
            if len(p) > k:
                heapq.heappop(p)
        return p[0]