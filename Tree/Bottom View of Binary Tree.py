class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution(object):
    def bottomView(self,root):
        def dfs(node,line,level):
            if not node:
                return
            if line not in m or level>=m[line][1]:
                m[line]=(node.val,level)
            dfs(node.left,line-1,level+1)
            dfs(node.right,line+1,level+1)
        m={}
        dfs(root,0,0)
        list1=[m[i][0] for i in sorted(m)]
        return list1
