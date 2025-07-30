class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution(object):
    def postorder(self,root):
        if not root:
            return []
        postorder=[]
        st1=[]
        st2=[]
        st1.append(root)
        while st1:
            node=st1.pop()
            st2.append(node)
            if node.left:
                st1.append(node.left)
            if node.right:
                st1.append(node.right)
        while st2:
            postorder.append(st2.pop().val)
        return postorder
