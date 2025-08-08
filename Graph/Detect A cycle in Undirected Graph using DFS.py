class Solution:
    def isCycle(self,V,edges):
        def dfs(node):
            if vis[node]==-1:
                return True
            elif vis[node]==1:
                return False
            vis[node]=-1
            for i in graph[node]:
                if dfs(i):
                    return True
            vis[node]=1
            return False
        graph=[[] for i in range(V)]
        vis=[0]*V
        for i,j in edges:
            graph[i].append(j)
        for i in range(V):
            if vis[i]==0:
                if dfs(i):
                    return True
        return False
