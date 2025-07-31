class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution(object):
    def isBalanced(self,root):
        def height(node):
            if not node:
                return 0
            lh=height(node.left)
            rh=height(node.right)
            if lh==-1 or rh==-1 or abs(lh-rh)>1:
                return -1
            return 1+max(lh,rh)
        return height(root)!=-1
