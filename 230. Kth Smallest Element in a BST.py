# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        self.in_order(root,res)
        return res[k-1]

    def in_order(self,root,num):
        if not root:
            return num
        self.in_order(root.left,num)
        num.append(root.val)
        self.in_order(root.right,num)