class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution(object):
    def boundary(self,root):
        def isLeaf(node):
            return not node.left and not node.right
        def addLeftBoundary(node,list1):
            cur=node.left
            while cur:
                if not isLeaf(cur):
                    list1.append(cur.val)
                if cur.left:
                    cur=cur.left
                else:
                    cur=cur.right
        def addRightBoundary(node,list1):
            cur=cur.right
            list2=[]
            while cur:
                if not isLeaf(cur):
                    list2.append(cur.val)
                if cur.right:
                    cur=cur.right
                else:
                    cur=cur.left
            list1.extend(reversed(list2))
        def addLeaves(node,list1):
            if isLeaf(node):
                list1.append(node.val)
                return
            if node.left:
                addLeaves(node.left,list1)
            if node.right:
                addLeaves(node.right,list1)
        if not root:
            return []
        list1=[]
        if not isLeaf(root):
            list1.append(root.val)
        addLeftBoundary(root,list1)
        addLeaves(root,list1)
        addRightBoundary(root,list1)
        return list1
