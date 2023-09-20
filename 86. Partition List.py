class Solution:
   """
   @param head: The first node of linked list
   @param x: An integer
   @return: A ListNode
   """
   def partition(self, head, x):

      dummy = ListNode("-inf")
      dummy.next = head 
      slow = dummy 
      fast = dummy
      
      while fast and fast.next:
      
         if fast.next.val >=x:# 找到partition的点
            fast = fast.next 
         else:
            if fast == slow:  # 没到partition时候快慢一起走
               fast = fast.next 
               slow = slow.next 
            else:
               temp = fast.next 
               fast.next = temp.next 
               temp.next = slow.next 
               slow.next = temp
               slow = temp # don't forget to move slow
      
      return dummy.next