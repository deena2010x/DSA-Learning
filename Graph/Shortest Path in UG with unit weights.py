from collections import deque
class Solution(object):
    def shortestPath(self,edges,N,M):
        graph=[[] for i in range(N)]
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        list1=[float('inf')]*N
        list1[0]=0
        queue=deque([0])
        while queue:
            node=queue.popleft()
            for i in graph[node]:
                if list1[node]+1<list1[i]:
                    list1[i]=list1[node]+1
                    queue.append(i)
        for i in range(N):
            if list1[i]==float('inf'):
                list1[i]=-1
        return list1
