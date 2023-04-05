from collections import deque

class Stack:
    
    def __init__(self):
        self.d = deque()

    def push(self,v):
        self.d.append(v)

    def pop(self):
        return self.d.pop()

    def __str__(self):
        return self.d.__str__()

    def __repr__(self):
        return self.d.__str__()



class Queue:
    def __init__(self):
        self.d = deque()

    def enqueue(self,v):
        pass

    def dequeue(self):
        pass
        
    
