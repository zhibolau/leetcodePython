# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        length = self.get_len(head)
        root, length = self.convert(head,length)
        return root

    def get_len(self,root):
        if not root: return 0
        length = 0
        while root:
            root = root.next
            length += 1
        return length
    
    def convert(self, head,length): #根据长度找到中间点
        if length == 0:
            return None, head
        
        left_root,middle = self.convert(head, length//2)
        right_root,next = self.convert(middle.next, length -length//2-1)

        root = TreeNode(middle.val) #中间点作为root
        root.left = left_root
        root.right = right_root
        return root,next
        



        