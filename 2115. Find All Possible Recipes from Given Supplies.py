class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        adj=defaultdict(list)
        ind=defaultdict(int)
        
        for i in range(len(ingredients)):
            for j in range(len(ingredients[i])):
                adj[ingredients[i][j]].append(recipes[i])
                ind[recipes[i]]+=1
        ans=[]
        q=deque()
        for i in range(len(supplies)):
            q.append(supplies[i])
        while q:
            node=q.popleft()
            for i in adj[node]:
                ind[i]-=1
                if ind[i]==0:
                    q.append(i)
                    ans.append(i)
        return ans