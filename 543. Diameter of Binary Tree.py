# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max = 0
        self.helper(root)
        return self.max
    def helper(self, root):
        if not root:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        self.max = max(self.max, left + right)
        return 1 + max(left, right)