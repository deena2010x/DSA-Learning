class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution(object):
    def succPredBST(self,root,key):
        pred=-1
        succ=-1
        node=root
        while node:
            if node.val==key:
                temp=node.left
                while temp and temp.right:
                    temp=temp.right
                if temp:
                    pred=temp.val
                temp=node.right
                while temp and temp.left:
                    temp=temp.left
                if temp:
                    succ=temp.val
                break
            elif node.val<key:
                pred=node.val
                node=node.right
            else:
                succ=node.val
                node=node.left
        return pred,succ
