class Solution(object):
    def dfsOfGraph(self,V,graph):
        def dfs(node):
            vis[node]=1
            result.append(node)
            for i in graph[node]:
                if not vis[i]:
                    dfs(i)
        vis=[0]*V
        result=[]
        dfs(0)
        return result
