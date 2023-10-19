class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = collections.defaultdict(list)
        in_degree = collections.defaultdict(int)
        for u, v in prerequisites:
            adj_list[v].append(u)    # [[1,0]], so that adj_list[0] = [1, ...]
            # in_degree
            in_degree[u] += 1
        
        # zero indegree queue
        queue = collections.deque()    
        for k in range(numCourses):
            if k not in in_degree:
                queue.append(k)       
        
        res = [] ### topological_sorted_order 
        while queue:
            vertex = queue.popleft()
            res.append(vertex)
                
            # Reduce in-degree for all the neighbors 
            if vertex in adj_list:
                for neighbor in adj_list[vertex]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)
            
        return res if len(res) == numCourses else []