class Solution(object):
    def findNumberOfComponents(self,e,V,edges):
        def dfs(node):
            vis[node]=1
            for i in graph[node]:
                if not vis[i]:
                    dfs(i)
        graph=[[] for i in range(V)]
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        vis=[0]*V
        count=0
        for i in range(V):
            if not vis[i]:
                dfs(i)
                count+=1
        return count
