class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution:
    def largestBST(self,root):
        def dfs(node):
            nonlocal max1
            if not node:
                return True,0,float('inf'),float('-inf')
            islBST,lsize,lmin,lmax=dfs(node.left)
            isrBST,rsize,rmin,rmax=dfs(node.right)
            if islBST and isrBST and lmax<node.val<rmin:
                size=lsize+rsize+1
                max1=max(max1,size)
                return True,size,min(lmin,node.val),max(rmax,node.val)
            return False,0,0,0
        max1=0
        dfs(root)
        return max1
