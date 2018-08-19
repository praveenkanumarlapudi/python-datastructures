class stack:
    def __init__(self):
        self.s = []
        self.top = -1
    
    def isStackEmpty(self):
        return self.top == -1
    
    def push(self,data):
        self.top = self.top + 1
        print(self.top)
        self.s.insert(data,self.top)
    
    def pop(self):
        if self.top >= 0:
            temp = self.top
            self.top = self.top - 1
            return self.s[temp]
        else:
            return "stack is empty"
    
    def peek(self):
        return self.s[self.top]
    
    def print_stack(self):
        print(self.s)


stack = stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
