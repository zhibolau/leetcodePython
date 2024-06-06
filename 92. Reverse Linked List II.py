
# 解法1

# 先将链表转化为列表, 然后将列表的m至n这一段反转, 之后再转化为链表.
# Time: 2* O(n)
# Space: O(1)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        l = []
        while head:
            l.append(head.val)
            head = head.next
        l[m-1:n] = l[m-1:n][::-1]
        dummy = p = ListNode(0)
        
        for val in l:
            p.next = ListNode(val)
            p = p.next
        return dummy.next




# 解法2

# 双指针法, 定义pre, cur两个指针, 将这两个指针向前移动m-1次, 然后反转n-m次.
# Time: O(n)
# Space: O(1)

class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        
        pre, cur = dummy, head
        for i in range(m-1):
            pre = pre.next
            cur = cur.next
        for j in range(n-m):
            temp = cur.next
            cur.next = temp.next
            temp.next = pre.next
            pre.next = temp
            
        return dummy.next
