class ArrayStack(object):
    def __init__(self):
        self.cap=1000
        self.st=[0]*self.cap
        self.top=-1

    def push(self,x):
        if self.top==self.cap-1:
            return
        self.top+=1
        self.st[self.top]=x

    def pop(self):
        if self.isEmpty():
            return -1
        val=self.st[self.top]
        self.top-=1
        return val

    def peek(self):
        if self.isEmpty():
            return -1
        return self.st[self.top]

    def isEmpty(self):
        return self.top==-1
