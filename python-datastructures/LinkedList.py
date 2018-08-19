class Node(object):
    def __init__(self,data):
        self.data = data
        self.nextNode = None
        
class LinkedList(object):
    
    def __init__(self):
        self.head = None
        self.size = 0
    #O(1)
    def insert_at_first(self,data):
        temp = Node(data)
        if not self.head:
            self.head = temp
        else:
            temp.nextNode = self.head
            self.head = temp
        self.size = self.size+1
        
    # O(1)    
    def size(self):
        return self.size
    # O(N)
    def insert_at_last(self, data):
        new_node = Node(data)
        temp = self.head
        self.size = self.size + 1
        
        while temp.nextNode is not None:
            temp = temp.nextNode
        temp.nextNode = new_node
    
    def remove_at_first(self):
        tempNode = self.head
        self.size = self.size - 1
        self.head = head.nextNode
        tempNode.nextNode = None
    
    def print_list(self):
        tempNode = self.head
        while tempNode.nextNode is not None:
            print("Element in the List is : " +str(tempNode.data))
    
    def remove(self,data):
        self.size = self.size - 1
        tempNode = self.head
        while tempNode.data != data:
                prevNode      = tempNode
                tempNode      = tempNode.nextNode
        prevNode.nextNode = tempNode.nextNode
        tempNode.nextNode = None
        
    
        
        
        
    