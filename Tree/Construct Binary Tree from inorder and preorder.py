class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution(object):
    def buildTree(self,preorder,inorder):
        def build(si,se,sp,ep):
            if si>se or sp>ep:
                return None
            rootVal=preorder[sp]
            root=TreeNode(rootVal)
            inRoot=m[rootVal]
            numsLeft=inRoot-si
            root.left=build(si,inRoot-1,sp+1,sp+numsLeft)
            root.right=build(inRoot+1,se,sp+numsLeft+1,ep)
            return root
        if len(inorder)!=len(preorder):
            return None
        m={val:i for i,val in enumerate(inorder)}
        return build(0,len(inorder)-1,0,len(preorder)-1)
