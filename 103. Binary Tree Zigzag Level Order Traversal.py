# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
       
        res = []
        self.pre_order(root,res,0) #0 is level
        return res

    def pre_order(self,root,res,level):
        if root:
            if len(res) <level+1:
                res.append([])
            if level % 2 ==0:
                res[level].append(root.val)
            else:
                res[level].insert(0,root.val)
            self.pre_order(root.left,res,level+1)
            self.pre_order(root.right,res,level+1)