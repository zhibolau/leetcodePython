# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        list_node =[]
        list_val =[]
        self.inorder(root,list_node,list_val)
        list_val.sort()
        for i in range(len(list_val)):
            list_node[i].val = list_val[i]
        return root
    
    def inorder(self,root,list_node,list_val):
        if not root:
            return
        self.inorder(root.left,list_node,list_val)
        list_node.append(root)
        list_val.append(root.val)
        self.inorder(root.right,list_node,list_val)