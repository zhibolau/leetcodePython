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
            if level % 2 ==0:  #偶数层直接放， left， right
                res[level].append(root.val)
            else:#奇数层倒着放 后来的放在前边，right，left
                res[level].insert(0,root.val)
            self.pre_order(root.left,res,level+1)
            self.pre_order(root.right,res,level+1)

#法2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return None
        res = []
        res1=[]
        q=deque()
        q.append(root)
        while q:
            level = []
            for _ in range(len(q)):
                node=q.popleft()
                level.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(level)
        for i,j in enumerate(res):
            if i%2 ==0:
                res1.append(j)
            else:
                res1.append(j[::-1])
        return res1