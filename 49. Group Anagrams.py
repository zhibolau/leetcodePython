class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for i in sorted(strs):
            sorted_i = ''.join(sorted(i)) #sorted 返回的是list， 得join才能变成str
            d[sorted_i] = d.get(sorted_i, [])+[i]
        return d.values()