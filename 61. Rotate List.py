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
        while tail: #计算链表长度
            tail = tail.next
            len+=1
        k = k % len
        if k ==0:# k是长度的倍数就不用翻转了
            return head
        for _ in range(k):
            fast = fast.next

        while fast.next: #k为slow与fast的距离  与删除倒数第几个node一样
            slow = slow.next
            fast = fast.next

        new_head = slow.next
        slow.next = None
        fast.next = head
        return new_head

        