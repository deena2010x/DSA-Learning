class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution(object):
    def rightSideView(self,root):
        def dfs(node,level):
            if not node:
                 return
            if level==len(list1):
                list1.append(node.val)
            dfs(node.right,level+1)
            dfs(node.left,level+1)
        list1=[]
        dfs(root,0)
        return list1
