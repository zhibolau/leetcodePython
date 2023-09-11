# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        fast = slow = head
        stack =[]
        while fast and fast.next: # fast->fast->none
            stack.append(slow.val) #不是所有的数字都会放入stack
            slow = slow.next
            fast = fast.next.next
        #1->slow->2->fast->none
        #stack has 1,2 要检查1，2是否与 2，fast一样，所以slow向后移动一位开始检查
        if fast:#没有fast的时候slow就在最末尾就没有next，所以要检查fast是否存在
            slow = slow.next #1->2>slow->fast  ;让slow去结尾 跟 第一个进入stack的数去比
        #1->2 在stack中
        while slow:
            top = stack.pop()
            if top != slow.val:
                return False
            slow = slow.next
        return True
        