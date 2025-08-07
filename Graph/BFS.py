from collections import deque
class Solution(object):
    def bfsOfGraph(self,V,graph):
        vis=[0]*V
        result=[]
        queue=deque([0])
        vis[0]=1
        while queue:
            node=queue.popleft()
            result.append(node)
            for i in graph[node]:
                if not vis[i]:
                    vis[i]=1
                    queue.append(i)
        return result
