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
      
         if fast.next.val >=x:# 小于x的时候就继续往前走
            fast = fast.next 
         else:
            if fast == slow:  # 小于x的时候就继续往前走
               fast = fast.next 
               slow = slow.next 
            else:
               temp = fast.next 
               fast.next = temp.next 
               temp.next = slow.next 
               slow.next = temp
               slow = temp # don't forget to move slow
      
      return dummy.next