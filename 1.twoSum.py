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
        
        #better dict
        dict = {}

        for i,j in enumerate(nums):
            if j not in dict: #已经遇到j了，下一次就要找target-j，所以遇到j了就直接拿到他的参数
                dict[target - j] = i #target -j 是因为我们希望遇到target-j，因为就找到了
            else:
                return [dict[j],i]
        


#method 2 brute force
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        x = 0

        for i in nums:
            x +=1
            for j in range(x,len(nums)):
                if i + nums[j] == target:
                    res.append(x-1) #注意i的index
                    res.append(j)
                    return res

