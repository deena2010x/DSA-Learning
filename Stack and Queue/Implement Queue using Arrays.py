class ArrayQueue:
    def __init__(self):
        self.cap=1000
        self.q=[0]*self.cap
        self.start=0
        self.end=0
        self.size=0

    def push(self,x):
        if self.size==self.cap:
            return
        self.q[self.end]=x
        self.end=(self.end+1)%self.cap
        self.size+=1

    def pop(self):
        if self.isEmpty():
            return -1
        val=self.q[self.start]
        self.start=(self.start+1)%self.cap
        self.size-=1
        return val

    def peek(self):
        if self.isEmpty():
          return -1
        return self.q[self.start]

    def isEmpty(self):
        return self.size==0
