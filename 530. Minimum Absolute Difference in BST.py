# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        nums = self.inTraversal(root, [])
        ans = min([abs(nums[i+1] - nums[i]) for i in range(len(nums)-1)])
        return ans

    def inTraversal(self, root, nums):
        if not root:return []
        self.inTraversal(root.left, nums)
        nums.append(root.val)
        self.inTraversal(root.right, nums)
        return nums


#BST用inorder traversal 之后就是排过序的数组。 任意node的最小只可能存在在inorder的邻接元素之间。 time: O(n), space: O(n)