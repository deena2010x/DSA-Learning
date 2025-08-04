class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution(object):
    def floorCeilOfBST(self,root,key):
        floor=-1
        ceil=-1
        node=root
        while node:
            if node.val==key:
                floor=ceil=node.val
                break
            elif node.val<key:
                floor=node.val
                node=node.right
            else:
                ceil=node.val
                node=node.left
        return floor,ceil
