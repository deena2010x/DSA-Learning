class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution(object):
    def bstFromPreorder(self,preorder):
        def build(bound):
            nonlocal i
            if i==len(preorder) or preorder[i]>bound:
                return None
            root=TreeNode(preorder[i])
            i+=1
            root.left=build(root.val)
            root.right=build(bound)
            return root
        i=0
        return build(float('inf'))
