class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution(object):
    def countNodes(self,root):
        def leftHeight(node):
            h=0
            while node:
                h+=1
                node=node.left
            return h
        def rightHeight(node):
            h=0
            while node:
                h+=1
                node=node.right
            return h
        if not root:
            return 0
        l=leftHeight(root)
        r=rightHeight(root)
        if l==r:
            return (1<<l)-1
        return 1+self.countNodes(root.left)+self.countNodes(root.right)
