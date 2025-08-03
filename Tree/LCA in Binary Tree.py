class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution(object):
    def lowestCommonAncestor(self,root,p,q):
        if not root or root==p or root==q:
            return root
        l=self.lowestCommonAncestor(root.left,p,q)
        r=self.lowestCommonAncestor(root.right,p,q)
        if l and r:
            return root
        return l if l else r
