from collections import deque
class Solution(object):
    def topoSort(self,V,graph):
        indegree=[0]*V
        for node in range(V):
            for i in graph[node]:
                indegree[i]+=1
        queue=deque()
        for i in range(V):
            if indegree[i]==0:
                queue.append(i)
        list1=[]
        while queue:
            node=queue.popleft()
            list1.append(node)
            for i in graph[node]:
                indegree[i]-=1
                if indegree[i]==0:
                    queue.append(i)
        return list1
