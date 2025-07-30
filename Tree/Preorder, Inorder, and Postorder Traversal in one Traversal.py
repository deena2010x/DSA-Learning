class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution(object):
    def tree_traversal(self,root):
        def traverse(node):
            if not node:
                return
            preorder.append(node.val)
            traverse(node.left)
            inorder.append(node.val)
            traverse(node.right)
            postorder.append(node.val)
        inorder=[]
        preorder=[]
        postorder=[]
        traverse(root)
        return [inorder,preorder,postorder]
