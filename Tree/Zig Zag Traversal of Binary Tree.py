class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution(object):
    def zigzagLevelOrder(self,root):
        def zigzag(node,level):
            if not node:
                return
            if len(list1)<=level:
                list1.append([])
            if level%2==0:
                list1[level].append(node.val)
            else:
                list1[level].insert(0,node.val)
            zigzag(node.left,level+1)
            zigzag(node.right,level+1)
        list1=[]
        zigzag(root,0)
        return list1
