# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.valid(root,float('-inf'),float('inf'))
        
    def valid(self, root, min,max):
        if not root:
            return True
        elif root.val >= max or root.val <=min: #等号不能忘记 因为可能都是一样的元素
            return False
        return self.valid(root.left,min,root.val) and self.valid(root.right,root.val,max)
        