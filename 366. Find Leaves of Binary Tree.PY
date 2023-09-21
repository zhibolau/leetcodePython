# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res =[]
        self.helper(root,res)
        return res
    def helper(self,root,res):
        if not root:
            return -1
        height = -1
        height = max(height,self.helper(root.left,res)+1) #ROOT自己高度为1
        height = max(height,self.helper(root.right,res)+1)
        if height>= len(res): #高度代表了res中的那层树的节点，比当前list的元素数量还多就是当前的元素不够装下这一层的元素了
            res.append([])
        res[height].append(root.val)
        return height

        