# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#1.最长条路径经过根节点，那么只需要找出根节点的左右两棵子树的最大深度然后相加即可。 
#2.最长路径没有经过根节点，那么只需要找出根节点的左子树或者根节点的右子树作为根的
#最长路径度即可。
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