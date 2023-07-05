# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not inorder: return None
        root_val = preorder[0] #get root value from preorder array
        root = TreeNode(root_val)
        rootPos = inorder.index(root_val) #get root index from inorder array
        #this index would tell the size of left or right tree

        #get  left tree of pre and inorder
        root.left = self.buildTree(preorder[1:rootPos+1],inorder[:rootPos])
        #get  right tree of pre and inorder
        root.right = self.buildTree(preorder[rootPos+1:],inorder[rootPos+1:])
        
        return root