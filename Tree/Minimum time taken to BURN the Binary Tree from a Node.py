from collections import deque
class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution(object):
    def timeToBurnTree(self,root,start):
        def markParents(node,parent=None):
            nonlocal startNode
            if not node:
                return
            if parent:
                parents[node]=parent
            if node.val==start:
                startNode=node
            markParents(node.left,node)
            markParents(node.right,node)
        parents={}
        vis=set()
        startNode=None
        markParents(root)
        q=deque([startNode])
        vis.add(startNode)
        time=0
        while q:
            for _ in range(len(q)):
                node=q.popleft()
                for i in (node.left,node.right,parents.get(node)):
                    if i and i not in vis:
                        vis.add(i)
                        q.append(i)
            if q:
                time+=1
        return time
