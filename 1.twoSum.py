class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        list = []
        for i in xrange(len(nums)):
            x = nums[i]
            if (target - x) in dict:
                list.append(dict[target -x])
                list.append(i)
                return list
            dict[x] = i
