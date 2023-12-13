class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        # q = deque()   
        # q.append(root)
        q=deque([root]) #也可以
        dummy=Node(-999) # to initialize with a not null prev
        while q:            
            prev=dummy
            for _ in range(len(q)): # iterate through all nodes in the same level
                popped=q.popleft()
                if popped.left:
                    q.append(popped.left)
                    prev.next=popped.left
                    prev=prev.next
                if popped.right:
                    q.append(popped.right)
                    prev.next=popped.right
                    prev=prev.next                
                 
        return root