class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        end = rightmost = step = 0

        for i in range(len(nums)):
            if i > rightmost: # rightmost 是当前数字能走到的最远index，再想往右走step就得+1
                step += 1
                rightmost = end #更新边界
            end = max(end, i+nums[i]) #更新下次层的边界

        return step
        