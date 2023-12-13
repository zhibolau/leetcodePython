"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
https://youtu.be/6YoQgdPZhHg
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root and root.left and root.right:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left #连接两个子节点的子节点（右和左 本来没有连接，又在同一层）
            self.connect(root.left)
            self.connect(root.right)
        return root


#看图可以写出