class node:
    def __init__(self,data):
        self.data = data
        self.leftchild = None
        self.rightchild = None
    
class bst:
    def __init__(self):
        self.root = None
    
    def insert(self,data):
        #new_node = node(data)
        if not self.root:
            self.root = node(data)
        else:
            self.insertNode(data,self.root)
    
    def insertNode(self,data,parentnode):
        if data < parentnode.data:
            if parentnode.leftchild:
                self.insertNode(data,parentnode.leftchild)
            else:
                parentnode.leftchild = node(data)
        else:
            if parentnode.rightchild:
                self.insertNode(data,parentnode.rightchild)
            else:
                parentnode.rightchild = node(data)
    
    def getMinValue(self):
        if self.root:
            return self.getMin(self.root)
        
    def getMin(self,node):
        if node.leftchild:
            return self.getMin(node.leftchild)
        return node.data
    
    def getMaxValue(self):
        if self.root:
            return self.getMax(self.root)
    
    def getMax(self,node):
        if node.rightchild:
            return self.getMax(node.rightchild)
        return node.data
    
    # Traversal ---
       # 1. Inorder -- left + root+ right O(N)
    def inorderTraversal(self):
        if self.root:
            self.inorder(self.root)
    
    def inorder(self,parentnode):
        if parentnode.leftchild:
            self.inorder(parentnode.leftchild)
        
        print(parentnode.data)
        
        if parentnode.rightchild:
            self.inorder(parentnode.rightchild)
        
         #2 Pre-Order -- root + left + right O(N)
    def preorderTraversal(self):
        if self.root:
            self.preorder(self.root)
    
    def preorder(self,node):
        print(node.data)
        
        if node.leftchild:
            self.preorder(node.leftchild)
        
        if node.rightchild:
            self.preorder(node.rightchild)
            
        #3 Post-order  -- left + right + root O(N)
    def postorderTraversal(self):
        if self.root:
            self.postorder(self.root)
        
    def postorder(self,node):
        if node.leftchild:
            self.postorder(node.leftchild)
        
        if node.rightchild:
            self.postorder(node.rightchild)
        print(node.data)
    
    def delete(self,data):
        if self.root:
            self.root = self.deleteNode(data,self.root)
    
    def deleteNode(self,data,d_node):
        if not d_node:
            return d_node
        
        if data > d_node.data:
            d_node.rightchild = self.deleteNode(data,d_node.rightchild)
        
        elif data < d_node.data:
            d_node.leftchild = self.deleteNode(data,d_node.leftchild)
        
        else:
            # leaf node
            if not d_node.rightchild and not d_node.leftchild:
                del d_node
                return None
            
            # only leftchild
            if not d_node.rightchild and d_leftchild:
                tempNode = d_node.leftchild
                del d_node
                return tempNode
            
            # only rightchild
            if d_node.rightchild and not d_leftchild:
                tempNode = d_node.rightchild
                del d_node
                return tempNode
            
            # Both childeren
            tempNode = self.getPredessor(d_node.left)
            node.data = tempNode.data
            d_node.leftchild = self.deleteNode(tempNode.data,d_node.leftchild)
            
            
            
                
        
            
        
        
    
bstree = bst()
bstree.insert(10)
bstree.insert(5)
bstree.insert(15)
bstree.insert(6)
bstree.insert(4)
bstree.insert(7)
#print(bstree.getMinValue())
#print(bstree.getMaxValue())
#bstree.inorderTraversal()
#bstree.preorderTraversal()
bstree.postorderTraversal()
bstree.delete(6)


        
            
        
                
  
        