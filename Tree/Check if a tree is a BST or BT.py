class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution:
    def isValidBST(self,root):
        def inorder(node):
            nonlocal prev
            if not node:
                return True
            if not inorder(node.left):
                return False
            if prev!=None and node.val<=prev:
                return False
            prev=node.val
            return inorder(node.right)
        prev=None
        return inorder(root)
