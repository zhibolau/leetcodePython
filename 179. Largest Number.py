from functools import cmp_to_key

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums.sort(key=cmp_to_key(lambda x, y: 1 if str(x)+str(y) < str(y)+str(x) else -1)) 
        #注意全序关系下，>表示升序，如果需要逆序reverse=True即可
        #比如 3 30，根据9行， 小的要排在前面，因为小于号；或者写成27行
        print(nums)
        if nums[0] == 0:
            return '0'
        return "".join([str(x) for x in nums])


#组成最大数字  返回str 保持原来顺序
# Input: nums = [3,30,34,5,9]
# Output: "9534330"
        

# a = Solution()
# print(a.largestNumber([1,13]))

#也可以写成这样
#nums.sort(key=cmp_to_key(lambda x,y: 1 if str(x)+str(y) >  str(y)+str(x) else -1),reverse=True)
#https://blog.csdn.net/weixin_46447549/article/details/128159867?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-0-128159867-blog-123118854.235^v38^pc_relevant_anti_vip_base&spm=1001.2101.3001.4242.1&utm_relevant_index=3