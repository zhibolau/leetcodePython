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
            while node.next and node.next.val == node.val: #有重复的要一直查看，一直略过才行
                node.next = node.next.next
            node = node.next
            prev.next = prev.next.next
        return dummy.next
    


#或者 continue容易忘就这么写
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p= d = ListNode(-1,head) #p mean prev
        node = head
        while node and node.next:
            if node.val != node.next.val:
                node=node.next
                p=p.next
            else:
                while node.next and node.val == node.next.val:
                    node.next=node.next.next
                node=node.next
                p.next=p.next.next
        return d.next