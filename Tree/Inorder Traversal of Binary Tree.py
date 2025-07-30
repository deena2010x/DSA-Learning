class TreeNode(object):
    def _init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution(object):
    def inorder(self,root):
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            inorder.append(node.val)
            dfs(node.right)
        inorder=[]
        dfs(root)
        return inorder
