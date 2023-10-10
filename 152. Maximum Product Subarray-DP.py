class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        global_max=prev_min=prev_max = nums[0]
        
        for num in nums[1:]:
            if num >0:
                curr_max = max(num,num * prev_max)
                curr_min = min(num,num * prev_min)
            else:
                curr_max = max(num,num * prev_min)
                curr_min = min(num,num * prev_max)
            global_max = max(curr_max,global_max)
            prev_max = curr_max
            prev_min = curr_min
        return global_max
        