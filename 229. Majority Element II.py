class Solution:
    """
    @param nums: A list of integers
    @return: The majority number occurs more than 1/3
    """
    def majorityNumber(self, nums):
        # write your code here
        table = {}
        for i, num in enumerate(nums):
            if num not in table:
                table[num] = 1
            else:
                table[num] += 1
        
        for key, value in table.items():
            if value > len(nums) // 3:
                return key