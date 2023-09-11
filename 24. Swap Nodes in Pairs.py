# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        temp = head.next
        head.next = self.swapPairs(head.next.next)
        temp.next= head
        return temp

        


#method 2
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        
        d = ListNode(0)
        d.next = head
        prev = d
        
        cur = head
        while cur and cur.next:
            prev.next = cur.next
            cur.next =prev.next.next
            prev.next.next=cur
            prev,cur= cur,cur.next
            
        return d.next