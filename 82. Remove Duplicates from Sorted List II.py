# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        node = head
        while node and node.next:
            if node.next and node.next.val != node.val:
                node= node.next
                prev = prev.next
                continue
            while node.next and node.next.val == node.val:
                node.next = node.next.next
            node = node.next
            prev.next = prev.next.next
        return dummy.next

        