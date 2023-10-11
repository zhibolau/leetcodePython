#可以过lc
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)<=1: return nums
        #从右向左扫过，寻找一个递增序列
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                for k in range(len(nums)-1,i,-1):
                    if nums[k]>nums[i]:
                        nums[i],nums[k]=nums[k],nums[i]
                        nums[i+1:]=sorted(nums[i+1:])
                        break
                break
            else: #nums[i]>nums[i+1]  nums整体降序
                if i==0: #[3,2,1]
                    nums.sort()
        return nums

#不能过lc  但是手动推导是对的
class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers
    """
    def nextPermutation(self, nums):
        # write your code here
        if not nums or len(nums) < 2:
            return nums
        i = len(nums) - 2
        while nums[i] >= nums[i+1]:
            i -= 1
            if i < 0: #[3,2,1] i一直在减少说明，从后看list时候，后面的元素一直比前面的小，是一个递减list
                return nums[::-1]
        j = len(nums) - 1
        while nums[j] <= nums[i]:# [2,3,1] 的字典序前一个为 2,1,3, 之后为 3,1,2 再来 3,2,1
            j -= 1  # 2,3,1 23对调后，3在最前，之后应该给字典序 也就是结果里的sorted
        nums[i], nums[j] = nums[j], nums[i] # [1，2，3]
        return nums[:i+1] + sorted(nums[i+1:])

#字典顺序