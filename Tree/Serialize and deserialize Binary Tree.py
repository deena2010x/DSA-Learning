class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution(object):
    def serialize(self,root):
        def dfs(node):
            if not node:
                list1.append("None")
                return
            list1.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        list1=[]
        dfs(root)
        return ','.join(list1)
    def deserialize(self,data):
        def dfs():
            val=next(list1)
            if val=="None":
                return None
            node=TreeNode(int(val))
            node.left=dfs()
            node.right=dfs()
            return node
        list1=iter(data.split(','))
        return dfs()
