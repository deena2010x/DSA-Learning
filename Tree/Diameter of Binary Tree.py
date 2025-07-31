class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution(object):
    def diameterOfBinaryTree(self,root):
        def diameter(node):
            nonlocal d
            if not node:
                return 0
            ld=diameter(node.left)
            rd=diameter(node.right)
            d=max(d,ld+rd)
            return 1+max(ld,rd)
        d=0
        diameter(root)
        return d
