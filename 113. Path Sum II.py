# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum1):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def find_path(root,path):
            if root.left is None and root.right is None and sum(path+[root.val]) == sum1:
                all.append(path+[root.val])
            
            if root.left: find_path(root.left,path+[root.val])
            if root.right: find_path(root.right,path+[root.val])
                
        all =[]
        if root:
            find_path(root,[])
        return all
    
        

        