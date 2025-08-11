from heapq import heappop,heappush
class Solution(object):
    def dijkstra(self,V,graph,S):
        list1=[float('inf')]*V
        list1[S]=0
        queue=[(0,S)]
        while queue:
            d,node=heappop(queue)
            if d>list1[node]:
                continue
            for i,j in graph[node]:
                if list1[node]+j<list1[i]:
                    list1[i]=list1[node]+j
                    heappush(queue,(list1[i],i))
        return list1
