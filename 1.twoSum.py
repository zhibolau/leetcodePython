class Solution(object):
    def twoSum(self, nums, target):
        """
        Given nums = [2, 7, 11, 15], target = 9,
        Because nums[0] + nums[1] = 2 + 7 = 9,
        return [0, 1].
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
