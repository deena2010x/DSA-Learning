class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution(object):
    def inorder(self,root):
        inorder=[]
        stack=[]
        node=root
        while True:
            if node:
                stack.append(node)
                node=node.left
            else:
                if not stack:
                    break
                node=stack.pop()
                inorder.append(node.val)
                node=node.right
        return inorder
