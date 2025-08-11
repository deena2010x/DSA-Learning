from heapq import heappop, heappush
class Solution:
    def shortestPath(self,N,M,edges):
        graph=[[] for i in range(N)]
        for i,j,k in edges:
            graph[i].append((j,k))
        list1=[float('inf')]*N
        list1[0]=0
        queue=[(0,0)]
        while queue:
            d,node=heappop(queue)
            if d>list1[node]:
                continue
            for i,j in graph[node]:
                if list1[node]+j<list1[i]:
                    list1[i]=list1[node]+j
                    heappush(queue,(list1[i],i))
        for i in range(N):
            if list1[i]==float('inf'):
                list1[i]=-1
        return list1
