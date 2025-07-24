class QueueStack(object):
    def __init__(self):
        self.q=deque()

    def push(self,x):
        n=len(self.q)
        self.q.append(x)
        for i in range(n):
            self.q.append(self.q.popleft())
            
    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def isEmpty(self):
        return not self.q
