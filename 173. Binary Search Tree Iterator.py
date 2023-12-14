# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
【解题思路】 
（1）初始化时从root开始一路向左走到最末端的节点，即全局最小值，
并将一路访问过的节点加入到stack中。 
（2）实现hasNext()：stack-1 一直存放 iterator 
指向的当前节点。因此在判断有没有下一个节点时，只需要判断 stack 是否为空。
（3）实现next()：弹出当前stack的栈顶元素（即所求的next节点），并将 stack 
 进行相应的变化，移动到下一个点。
  
 找到下一个点的算法为： 
 如果当前点存在右子树，那么下一节点就是其右子树中一路向左走到底的那个点，
 并且需要把路上经过的节点加入stack（因为这些节点都比下一个节点大，尚未访问过）；
 
 如果当前点不存在右子树，则弹出当前节点后新的栈顶（如果不为空的话）自然就是下一个节点。
"""
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left #找到最小值
        
    def next(self):
        """
        :rtype: int
        """
        if self.stack:
            root = self.stack.pop()
            node = root.right
            while node:
                self.stack.append(node)
                node = node.left
            return root.val

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.stack
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()