class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        h = []
        for n1 in nums1:
            for n2 in nums2:
                heapq.heappush(h, (n1+n2, n1, n2))
                
        res=[]
        for _ in range(k):
            if h:
                _, u, v = heapq.heappop(h)
                res.append([u, v])
        return res