class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution(object):
    def buildTree(self,inorder,postorder):
        def build(si,ei,sp,ep):
            if si>ei or sp>ep:
                return None
            rootVal=postorder[ep]
            root=TreeNode(rootVal)
            inRoot=m[rootVal]
            numsLeft=inRoot-si
            root.left=build(si,inRoot-1,sp,sp+numsLeft-1)
            root.right=build(inRoot+1,ei,sp+numsLeft,ep-1)
            return root
        if len(inorder)!=len(postorder):
            return None
        m={val:i for i,val in enumerate(inorder)}
        return build(0,len(inorder)-1,0,len(postorder)-1)
