class Solution:
    """
    @param nums: the list
    @return: the sum of all paths from the root towards the leaves
    """
    def pathSumIV(self, nums):
        # Write your code here.
        if len(nums) == 1:	
            return nums[0] % 10;        
        a = [-1 for i in range(100)];
        for i in nums:
            a[i / 10] = i % 10;
        ret = 0;
        for i in range(2,5):
            for j in range(1,9):
                idx = i * 10 + j;
                pre = (i - 1) * 10 + (j + 1)/2;
                next1 = (i + 1) * 10 + 2 * j;
                next2 = (i + 1) * 10 + 2 * j - 1;
                if a[idx] != -1 and a[pre] != -1: 
                    a[idx] = a[idx] + a[pre];        		
                if a[next1] == -1 and a[next2] == -1 and a[idx] != -1:
                    ret = ret + a[idx];        	
        return ret;