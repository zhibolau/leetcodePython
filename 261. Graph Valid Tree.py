class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) !=n-1: 
            return False
        neighbors=collections.defaultdict(list)
        for u,v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)
        visited={}
        queue=deque()
        queue.append(0)
        visited[0]=True
        while len(queue) != 0:
            cur=queue.popleft()
            visited[cur]=True
            for i in neighbors[cur]:
                if i not in visited:
                    visited[i]=True
                    queue.append(i)
                    
        return len(visited)==n
            