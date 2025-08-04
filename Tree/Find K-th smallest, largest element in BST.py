class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution:
    def kthSmallest(self,root,k):
        def inorder(node):
            nonlocal count,ans
            if not node or ans!=None:
                return
            inorder(node.left)
            count+=1
            if count==k:
                ans=node.val
                return
            inorder(node.right)
        count=0
        ans=None
        inorder(root)
        return ans
