class Solution(object):
    def findCircleNum(self,graph):
        def dfs(node):
            vis[node]=1
            for i in range(V):
                if graph[node][i]==1 and not vis[i]:
                    dfs(i)
        V=len(graph)
        vis=[0]*V
        count=0
        for i in range(V):
            if not vis[i]:
                dfs(i)
                count+=1
        return count
