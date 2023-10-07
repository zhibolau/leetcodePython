# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if not root:
            return True
        
        return self.sym_re(root.left,root.right)
    
    def sym_re(self,l,r):
        if l is None and r is None:
            return True
        if l is None or r is None or l.val != r.val:
            return False
        
        return self.sym_re(l.left, r.right) and self.sym_re(l.right, r.left) # 看例子图比较好写出来
    


    #method 2 stack
def isSymmetric(self, root):
        if not root:
            return True
        s = []
        s.append(root.left)
        s.append(root.right)
        while s:
            l_node = s.pop()
            r_node = s.pop()
            if l_node is None and r_node is None:
                continue
            if l_node is None or r_node is None:
                return False
            if l_node.val != r_node.val:
                return False
            s.append(l_node.left)
            s.append(r_node.right)

            s.append(l_node.right)
            s.append(r_node.left)

        return True
