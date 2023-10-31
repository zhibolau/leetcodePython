class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        for i in nums:
            d[i]=d.get(i,0) +1

        sort_nums=sorted(d.items(), key=lambda x: x[1],reverse=True)

        res = []
        for i in range(k):
            res.append(sort_nums[i][0])

        return res