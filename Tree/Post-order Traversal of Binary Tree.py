class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution(object):
    def postorder(self,root):
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            postorder.append(node.val)
        postorder=[]
        dfs(root)
        return postorder
