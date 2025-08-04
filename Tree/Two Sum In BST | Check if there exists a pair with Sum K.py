class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution(object):
    def findTarget(self,root,k):
        def dfs(node):
            if not node:
                return False
            if k-node.val in vis:
                return True
            vis.add(node.val)
            return dfs(node.left) or dfs(node.right)
        vis=set()
        return dfs(root)
