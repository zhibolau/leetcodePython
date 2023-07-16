# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        max_v = max(p.val, q.val)
        min_v = min(p.val, q.val)
        while root:
            if root.val > max_v: #最终找的值实在pq之间的，比max大 就要去左边
                root = root.left
            elif root.val < min_v:
                root = root.right
            else:
                return root