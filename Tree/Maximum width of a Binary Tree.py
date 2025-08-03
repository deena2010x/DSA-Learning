class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution(object):
    def widthOfBinaryTree(self,root):
        def dfs(node,depth,index):
            nonlocal max1
            if not node:
                return
            if depth not in left:
                left[depth]=index
            max1=max(max1,index-left[depth]+1)
            dfs(node.left,depth+1,2*index)
            dfs(node.right,depth+1,2*index+1)
        left={}
        max1=0
        dfs(root,0,0)
        return max1
