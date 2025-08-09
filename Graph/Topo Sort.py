class Solution(object):
    def topoSort(self,V,graph):
        def dfs(node):
            vis[node]=1
            for i in graph[node]:
                if not vis[i]:
                    dfs(i)
            stack.append(i)
        vis=[0]*V
        stack=[]
        for i in range(V):
            if not vis[i]:
                dfs(i)
        return stack[::-1]
