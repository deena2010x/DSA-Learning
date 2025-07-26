class MinStack(object):
    def __init__(self):
        self.st=[]

    def push(self,val):
        if not self.st:
            self.st.append((val,val))
        else:
            self.st.append((val,min(val,self.st[-1][1])))

    def pop(self):
        if self.st:
            self.st.pop()

    def top(self):
        if self.st:
            return self.st[-1][0]

    def getMin(self):
        if self.st:
            return self.st[-1][1]
