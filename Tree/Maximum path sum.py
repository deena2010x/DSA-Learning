class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution(object):
    def maxPathSum(self,root):
        def path(node):
            nonlocal p
            if not node:
                return 0
            ls=max(0,path(node.left))
            rs=max(0,path(node.right))
            p=max(p,ls+rs+node.val)
            return max(ls,rs)+node.val
        p=float('-inf')
        path(root)
        return p
