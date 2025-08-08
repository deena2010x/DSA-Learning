from collections import deque
class Solution:
    def isCycle(self,V,edges):
        graph=[[]for i in range(V)]
        indegree=[0]*V
        for i,j in edges:
            graph[i].append(j)
            indegree[j]+=1
        queue=deque()
        for i in range(V):
            if indegree[i]==0:
                queue.append(i)
        count=0
        while queue:
            node=queue.popleft()
            count+=1
            for i in graph[node]:
                indegree[i]-=1
                if indegree[i]==0:
                    queue.append(i)
        return count!=V
