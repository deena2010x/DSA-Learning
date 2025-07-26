class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class LinkedListStack(object):
    def __init__(self):
        self.top_node=None

    def push(self,x):
        new=Node(x)
        new.next=self.top_node
        self.top_node=new

    def pop(self):
        if self.isEmpty():
            return None
        val=self.top_node.val
        self.top_node=self.top_node.next
        return val

    def top(self):
        if self.isEmpty():
            return None
        return self.top_node.val

    def isEmpty(self):
        return self.top_node==None
