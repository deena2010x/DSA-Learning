class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution(object):
    def recoverTree(self,root):
        def inorder(node):
            nonlocal first,second,prev
            if not node:
                return
            inorder(node.left)
            if prev and prev.val>node.val:
                if not first:
                    first=prev
                second=node
            prev=node
            inorder(node.right)
        first=second=prev=None
        inorder(root)
        if first and second:
            first.val,second.val=second.val,first.val
