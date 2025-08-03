class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution(object):
    def inorder(self,root):
        list1=[]
        cur=root
        while cur:
            if not cur.left:
                list1.append(cur.val)
                cur=cur.right
            else:
                prev=cur.left
                while prev.right and prev.right!=cur:
                    prev=prev.right
                if not prev.right:
                    prev.right=cur
                    cur=cur.left
                else:
                    prev.right=None
                    list1.append(cur.val)
                    cur=cur.right
        return list1
