class Solution(object):
    def canFinish(self,n,edges):
        def dfs(node):
            if vis[node]==-1:
                return False
            elif vis[node]==1:
                return True
            vis[node]=-1
            for i in graph[node]:
                if not dfs(i):
                    return False
            vis[node]=1
            return True
        graph=[[] for i in range(n)]
        vis=[0]*n
        for i,j in edges:
            graph[j].append(i)
        for i in range(n):
            if not dfs(i):
                return False
        return True
