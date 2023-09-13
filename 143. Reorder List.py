# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #找到中间节点 middle slow = middle.next 
    # 翻转从 slow 到最后的所有节点 将翻转后的节点和原来的节点merge
    # 需要注意要重新将 middle.next 赋值为 None
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        
        middle = self.middle(head)
        slow = self.reverse(middle.next)
        middle.next = None

        return self.merge(head,slow)

    def middle(self,head):
        fast = slow = head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def reverse(self, head):
        cur = None
        while head:
            temp = head.next
            head.next = cur
            cur = head
            head = temp
        return cur

    def merge(self,s, t):
        dummy = ListNode(0,s)
        while s and t:
            tmp_s = s.next
            tmp_t = t.next

            s.next = t
            t.next = tmp_s

            s = tmp_s
            t = tmp_t
        return dummy.next



