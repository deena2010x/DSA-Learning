class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution(object):
    def preorder(self,root):
        def dfs(node):
            if not node:
                return
            preorder.append(node.val)
            dfs(node.left)
            dfs(node.right)
        preorder=[]
        dfs(root)
        return preorder
