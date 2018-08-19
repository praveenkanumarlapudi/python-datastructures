class queue:
    def __init__(self):
        self.q = []
        self.front = -1
        self.last = -1
    
    def isEmpty(self):
        return self.q == []
    
    def enqueue(self,data):
        if self.last == -1:
            self.front = self.front + 1
        self.last = self.last + 1
        print("Inserting : ..."+str(data))
        self.q.insert(data,self.last)
        
    def dequeue(self):
        if self.last > self.first:
            temp = self.last
            self.first = self.first + 1
            return self.q[temp]
        else:
             return "Queue is Empty"
    
    def peek(self):
        return self.q[self.first]
    
    def print_queue(self):
        print(self.q)

queue = queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.print_queue()           
            