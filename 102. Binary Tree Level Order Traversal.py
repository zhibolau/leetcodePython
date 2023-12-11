# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None

        q,result = collections.deque(root), []
        while q:
            level = [] #记录每一层的数值

            for _ in range(len(q)):
                node = q.popleft() #清空当前层的q中的每一个node
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(level)
        
        return result
            

#easy版

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return None
        q=deque()
        res=[]

        q.append(root)
        while q:
            tmp=[]
            for _ in range(len(q)):
                n=q.popleft()
                tmp.append(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            res.append(tmp)

        return res

        