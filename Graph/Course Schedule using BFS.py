class Solution:
    def canFinish(self,n,edges):
        graph=[[] for i in range(n)]
        indegree=[0]*n
        for i,j in edges:
            graph[j].append(i)
            indegree[i]+=1
        queue=deque()
        for i in range(n):
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
        return count==n
