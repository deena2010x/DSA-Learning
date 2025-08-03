class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution(object):
    def distanceK(self,root,target,k):
        def markParents(node,parent=None):
            if not node:
                return
            if parent:
                parents[node]=parent
            markParents(node.left,node)
            markParents(node.right,node)
        def dfs(node,prev,d):
            if not node or node in vis:
                return
            vis.add(node)
            if d==k:
                list1.append(node.val)
                return
            for i in (node.left,node.right,parents.get(node)):
                if i!=prev:
                    dfs(i,node,d+1)
        list1=[]
        parents={}
        vis=set()
        markParents(root)
        dfs(target,None,0)
        return list1
