class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution(object):
    def checkChildrenSum(self,root):
        if not root or (not root.left and not root.right):
            return True
        l=root.left.val if root.left else 0
        r=root.right.val if root.right else 0
        if root.val!=l+r:
            return False
        return self.checkChildrenSum(root.left) and self.checkChildrenSum(root.right)
