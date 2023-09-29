# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.fla_return(root)
    def fla_return(self,root):
        if not root: return None
        left_last = self.fla_return(root.left)
        right_last = self.fla_return(root.right)
        if left_last: #把 2 左3 右4 变成  2 右3 3右4 
            left_last.right = root.right
            root.right= root.left
            root.left = None
        return right_last or left_last or root


        
        