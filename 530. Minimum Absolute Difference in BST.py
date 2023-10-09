# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
#         nums = self.in_order_traversal(root)
        
#         ans = abs(nums[1]-num[0])
#         for i in range(2,len(nums)):
#             ans = min(ans, abs(nums[i] - nums[i+1]))
#         return ans
#     def in_order_traversal(self,root):
#         if not root:
#             return []
#         res =[]
#         self.in_order_traversal(root.left)
#         res.append(root.val)
#         self.in_order_traversal(root.right)
#         return res
        nums = []
        self.preTraversal(root, nums)
        kkk =sorted(nums)
        print kkk
        ans = kkk[1] - kkk[0]
        for i in range(2, len(kkk)):
            ans = min(ans, kkk[i] - kkk[i - 1])
        return ans

    def preTraversal(self, root, nums):
        if not root:
            return
        nums.append(root.val)
        self.preTraversal(root.left, nums)
        
        self.preTraversal(root.right, nums)


#BST用inorder traversal 之后就是排过序的数组。 任意node的最小只可能存在在inorder的邻接元素之间。 time: O(n), space: O(n)