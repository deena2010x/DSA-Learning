class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class BSTIterator(object):
    def __init__(self,root):
        self.stack=[]
        node=root
        while node:
            self.stack.append(node)
            node=node.left
    def next(self):
        node=self.stack.pop()
        val=node.val
        node=node.right
        while node:
            self.stack.append(node)
            node=node.left
        return val
    def hasNext(self):
        return len(self.stack)>0
