# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: #整个树走一遍 加入list中 看个数
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:return 0
        temp = []
        self.traverse(root,temp)
        return len(temp)
    def traverse(self,root,temp):
        if not root:return 0
        self.traverse(root.left,temp)
        temp.append(root.val)
        self.traverse(root.right,temp)


        