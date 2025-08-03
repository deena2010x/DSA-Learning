class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution(object):
    def uniqueBinaryTree(self,a,b):
        set1={(1,2),(2,1),(2,3),(3,2)}
        if (a,b) in set1:
            return True
        return False
