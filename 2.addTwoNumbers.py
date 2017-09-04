# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        the digits are stored in reverse order
        Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
        Output: 7 -> 0 -> 8
        """
        d = ListNode(0)
        p = d
        flag = 0
        if l1 == None: return l2
        if l2 == None: return l1
        while l1 and l2:
            p.next = ListNode((l1.val+l2.val+flag)%10)
            flag = (l1.val+l2.val+flag)/10
            l1 = l1.next
            l2 = l2.next
            p = p.next
        if l2:
            while l2:
                p.next = ListNode((l2.val+flag)%10)
                flag = (l2.val+flag)/10
                l2 = l2.next
                p = p.next
        if l1:
            while l1:
                p.next = ListNode((l1.val+flag)%10)
                flag = (l1.val+flag)/10
                l1 = l1.next
                p = p.next
        if flag == 1: p.next = ListNode(1)
        return d.next    