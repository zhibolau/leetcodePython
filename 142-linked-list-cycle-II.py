# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # if head == None or head.next == None:
        #     return None
        # slow,fast = head,head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        #     if slow == fast:
        #         break
        # if slow == fast:
        #     slow = head
        #     while slow != fast:
        #         slow = slow.next
        #         fast = fast.next
        #     return slow
        
        # return None

        
        if head == None or head.next == None:
            return None
        slow=fast=head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        
        if slow == fast:
            slow = head
            while fast != slow:
                slow = slow.next
                fast = fast.next
            return slow
        #return None


