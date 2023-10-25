#https://blog.csdn.net/zxzxzx0119/article/details/82889998
"""要处理线性复杂度的排序，可以用桶排序。

开三个数组，exist, max_num, min_num分别表示一个桶是否为空，桶里元素的最大值和桶里元素的最小值，

将nums里的每个数映射入桶之后，找到相邻两个非空桶的最大最小值之差。

找出数组得最大值max_val和最小值min_val
每个桶的宽度为size=（max_val-min_val)/(n-1)，并向上取整，一共n+1个桶，最后一个桶存最大值，
n个数放在n+1个桶，必然存在空桶，最大间距必然不来自同一个桶
把每个数都放进各自的桶里，nums[i]应该放在第(nums[i]-min_val)//size个桶里，
每个桶只存储该桶内的最小值和最大值，格式为[min,max]
排除掉空桶后，求相邻两个桶内数字的最大距离，即第i个桶的最小值和第i-1个桶的最大值之间的差

"""
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        min_val, max_val = min(nums), max(nums)
        if min_val == max_val:
            return 0
        
        n = len(nums) + 1 # 桶的个数
        step = (max_val - min_val) // n
        
        exist = [0 for _ in range(n + 1)]  #表示桶是否为空
        max_num = [0 for _ in range(n + 1)]#表示桶里元素的最大值
        min_num = [0 for _ in range(n + 1)]#表示桶里元素的最小值
        
        for num in nums: #把所有的数入桶
            idx = int((num - min_val) * n / (max_val - min_val)) #当前数与min的距离 占据 max-min 的比例 来决定index
            max_num[idx] = num if not exist[idx] else max(num, max_num[idx]) #exist[idx] =0 means false
            min_num[idx] = num if not exist[idx] else min(num, min_num[idx])
            exist[idx] = 1
        res = 0
        pre = max_num[0]
        for i in range(1, n + 1):
            if exist[i]:
                res = max(res, min_num[i] - pre)
                pre = max_num[i]
        return res
            
    #非线性

    class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        nums.sort()
        res = 0
        for i, num in enumerate(nums):
            if i > 0:
                res = max(res, num - nums[i - 1])
        return res