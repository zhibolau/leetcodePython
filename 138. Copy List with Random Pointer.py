"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        m = {} #dict
        cur = head
        while cur: #cur在动 head没动
            m[cur] =Node(cur.val) #m记录 当前node与只有当前node值的mapping
            cur = cur.next
        for n in m:
            if n.next:
                m[n].next = m[n.next] 
            if n.random:
                m[n].random = m[n.random]
        return m[head]

        