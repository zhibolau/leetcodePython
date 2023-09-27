class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_len, d = 0,{num:True for num in nums}

        for lo in nums:
            if lo -1 not in d:
                hi = lo + 1
                while hi in d:
                    hi += 1
                max_len= max(max_len,hi-lo)

        return max_len