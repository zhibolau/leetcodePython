"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @paramn n: An integer
    # @return: A list of root
    def generateTrees(self, n):
        return self.helper(1, n)
    
    # 返回值是从start到end的所有可能的二叉查找树
    def helper(self, start, end):
        if start > end:
            return [None]
        
        result = []
        # 枚举根节点的值
        for root_val in range(start, end + 1):
            # 递归获得所有可能的左子树
            left_trees = self.helper(start, root_val - 1)
            # 递归获得所有可能的右子树
            right_trees = self.helper(root_val + 1, end)
            # 枚举每一种左右子树的组合，组成新的二叉树
            for left_tree in left_trees:
                for right_tree in right_trees:
                    root = TreeNode(root_val)
                    root.left = left_tree
                    root.right = right_tree
                    result.append(root)
        
        return result