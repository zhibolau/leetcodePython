# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # pre order , then reverse
        if not root:
            return None
        
        res =[]
        
        self.dfs(root,res,0)
        
        return reversed(res)
    
    def dfs(self,root,res,level):
        if root:
            if len(res) < level +1:
                res.append([])
            res[level].append(root.val)
            
            self.dfs(root.left,res,level+1)
            self.dfs(root.right,res,level+1)
        