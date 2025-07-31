class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution(object):
    def verticalTraversal(self,root):
        def dfs(node,line,level):
            if not node:
                return
            m[line].append((level,node.val))
            dfs(node.left,line-1,level+1)
            dfs(node.right,line+1,level+1)
        m=defaultdict(list)
        list1=[]
        dfs(root,0,0)
        for line in sorted(m.keys()):
            list1.append([val for level,val in sorted(m[line])])
        return list1
