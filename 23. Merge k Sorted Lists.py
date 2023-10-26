# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from heapq import heappop,heappush
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) <1 :
            return None
        
        dum = tail = ListNode(-1)
        heap = []
        for node in lists:
            if node:
                heappush(heap,(node.val, node))
        
        while len(heap) > 0:
            cur = heappop(heap)[1]
            tail.next = cur
            tail = tail.next
            if cur.next:
                heappush(heap,(cur.next.val, cur.next))
        return dum.next
    
#tim method
    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(None)
        tail, heap = dummy, []
        
        for index, head in enumerate(lists):
            if not head: continue
            heappush(heap, (head.val, index, head))
            
        while heap:
            _, index, head = heappop(heap)
            tail.next, tail = head, head
            if head.next:
                heappush(heap, (head.next.val, index, head.next))
                
        return dummy.next
    

#method 3 merge

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        if not lists:
            return None
        
        return self.merge_range_lists(lists, 0, len(lists) - 1)
        
    def merge_range_lists(self, lists, start, end):
        if start == end:
            return lists[start]
        
        mid = (start + end) // 2
        left = self.merge_range_lists(lists, start, mid)
        right = self.merge_range_lists(lists, mid + 1, end)
        return self.merge_two_lists(left, right)
        
    def merge_two_lists(self, head1, head2):
        tail = dummy = ListNode(0)
        while head1 and head2:
            if head1.val < head2.val:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next
            
        if head1:
            tail.next = head1
        if head2:
            tail.next = head2
        
        return dummy.next