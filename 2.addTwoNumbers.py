# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        flag =0
        d =ListNode(-1)
        p = d
        if not l1:
            return l2
        if not l2:
            return l1
        while l1 and l2:
            p.next = ListNode((l1.val+l2.val+flag)%10)
            flag = int((l1.val+l2.val+flag)/10) #相加大于10 的就得进位
            l1=l1.next
            l2=l2.next
            p=p.next
        if l1:
            while l1:
                p.next = ListNode((l1.val+flag)%10)
                flag = int((l1.val+flag)/10) #不加int会出现小数
                l1=l1.next
                p=p.next
        if l2:
            while l2:
                p.next = ListNode((l2.val+flag)%10)
                flag = int((l2.val+flag)/10)
                l2=l2.next
                p=p.next
        if flag == 1: p.next=ListNode(1)
        return d.next

        