"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        def dfs(id):
            res = d[id][0] # importance
            for s in d[id][1]: #sub directS
                res += dfs(s)
            return res


        d = {}

        for i in employees:
            d[i.id] = [i.importance, i.subordinates]
        return dfs(id) if id in d else 0
        