# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #slow & fast pointers similar to 174 ####### #######

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next:
            return head
        len = 0
        
        tail= fast = slow = head
        while tail:
            tail = tail.next
            len+=1
        k = k % len
        if k ==0:
            return head
        for _ in range(k):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        new_head = slow.next
        slow.next = None
        fast.next = head
        return new_head

        