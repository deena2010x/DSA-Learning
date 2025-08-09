class Solution(object):
    def isBipartite(self,graph):
        def dfs(node,c):
            color[node]=c
            for i in graph[node]:
                if color[i]==-1:
                    if not dfs(i,1-c):
                        return False
                elif color[i]==c:
                    return False
            return True
        V=len(graph)
        color=[-1]*V
        for i in range(V):
            if color[i]==-1:
                if not dfs(i,0):
                    return False
        return True
