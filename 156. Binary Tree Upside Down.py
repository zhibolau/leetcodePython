
    
#recur
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: new root
    """
    def upsideDownBinaryTree(self, root):
        if root is None:
            return None
        return self.dfs(root)
        
    def dfs(self, root):
        if root.left is None:
            return root
        newRoot = self.dfs(root.left)
        root.left.right = root #看图可以写出
        root.left.left = root.right
        root.left = None
        root.right = None
        
        return newRoot
    

#iteration
class Solution:
    """
    @param root: the root of binary tree
    @return: new root
    """
    def upsideDownBinaryTree(self, root):
        # write your code here

        # this idea is similar to flip linked list
        if not root:
          return None

        prev = None
        prev_right = None
        head = root
        while head:
          # store temp
          temp_left = head.left
          temp_right = head.right
          # flip
          head.left=prev_right
          head.right = prev
          # move next
          prev = head #之前走过的点
          prev_right = temp_right #之前的右为 暂时的右
          head = temp_left # head根据题意为temp——left

        return prev