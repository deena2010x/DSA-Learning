class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class LinkedListQueue:
    def __init__(self):
        self.start=None
        self.end=None

    def push(self,x):
        new=Node(x)
        if self.end:
            self.end.next=new
        else:
            self.start=new
        self.end=new

    def pop(self):
        if self.isEmpty():
            return None
        val=self.start.val
        self.start=self.start.next
        if self.start==None:
            self.end=None
        return val

    def peek(self):
        if self.isEmpty():
            return None
        return self.start.val

    def isEmpty(self):
        return self.start==None
