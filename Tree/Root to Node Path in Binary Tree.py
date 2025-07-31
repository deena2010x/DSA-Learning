class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution(object):
    def allRootToLeaf(self,root):
        def dfs(node,path,list1):
            if not node:
                return
            path.append(node.val)
            if not node.left and not node.right:
                list1.append(list(path))
            else:
                dfs(node.left,path,list1)
                dfs(node.right,path,list1)
            path.pop()
        list1=[]
        dfs(root,[],list1)
        return list1
