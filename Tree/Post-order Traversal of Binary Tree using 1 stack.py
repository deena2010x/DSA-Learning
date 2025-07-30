class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution(object):
    def postorder(self,root):
        postorder=[]
        stack=[]
        lvis=root
        node=root
        while stack or node:
            if node:
                stack.append(node)
                node=node.left
            else:
                peek=stack[-1]
                if peek.right and lvis!=peek.right:
                    node=peek.right
                else:
                    stack.pop()
                    postorder.append(peek.val)
                    lvis=peek
        return postorder
