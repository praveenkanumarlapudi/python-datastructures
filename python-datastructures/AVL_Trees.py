class Node:
    def __init__(self, data):
        self.data   = data
        self.left   = None
        self.right  = None
        self.height = 0
    
class AVL:
    def __init__(self):
        self.root = None
    
    def calcHeight(self, node):
        if not node:
            return -1
        return node.height
    
    # if result of below method is:
    #                               > 1 then it is a left heavy tree and needs a 'Right Rotation'
    #                               < 1 then it is a right heavy tree and needs a 'left rotation'
    
    def checkIfBalanced(self, node):
        if not node:
            return -1
        return self.checkIfBalanced(node.left) - self.checkIfBalanced(node.right)
    
    def inorderTraverse(self):
        if self.root:
            self.inorder(self.root)
    
    def inorder(self, node):
        if node.left:
            self.inorder(node.left)
        print(node.data)
        if node.right:
            self.inorder(node.right)
        
        
    
    def rotateRight(self, node):
        
        tempLeftchild = node.left
        t = tempLeftchild.right
        
        tempLeftchild.right = node
        node.left = t
        
        node.height            = max(self.calcHeight(node.left),self.calcHeight(node.right)) + 1
        tempLeftchild.height   = max(self.calcHeight(tempLeftchild.left),self.calcHeight(tempLeftchild.right)) + 1
        return tempLeftchild
    
    def rotateLeft(self, node):
        
        tempRightchild = node.right
        t = tempRightchild.left
        
        tempRightchild.left = node
        node.right = t
        
        node.height = max(self.calcHeight(node.left),self.calcHeight(node.right)) + 1
        tempRightchild.height = max(self.calcHeight(tempRightchild.left),self.calcHeight(tempRightchild.right)) + 1
        
        return tempRightchild
    
    def insert(self, data):
        self.root = self.insertNode(self.root, data)
    
    def insertNode(self, node, data):
        if not node:
            return Node(data)
        if data > node.data:
            node.right = self.insertNode(node.right, data)
        else:
            node.left = self.insertNode(node.left, data)
        
        node.height = max(self.calcHeight(node.left),self.calcHeight(node.right)) + 1
        
        return self.settleViolations(data, node)
    
    def settleViolations(self,data, node):
        balance = self.checkIfBalanced(node)
        
        # Case 1 - Left Heavy situation Bal > 1
        
        if balance > 1 and data < node.left.data:
            return self.rotateRight(node)
        
        #case 2 - Right Heavy Bal < 1
        
        if balance < -1 and data > node.right.data:
            return self.rotateLeft(node)
        
        # Case 3 - Left Right Heavy -- Bal > 1 and node.left.data < data
        
        if balance > 1 and data > node.lef.data:
            node.left = self.rotateLeft(node.left)
            return self.rotateRight(node)
        
        # case 4 - right left heavy - bal < 1 and node.right.data > data
        
        if balance < -1 and data < node.right.data:
            node.right = self.rotateRight(node.right)
            return self.rotateLeft(node)
        return node
    
    
        
        
         
avl = AVL()
avl.insert(5)
avl.insert(3)
avl.insert(4)
avl.inorderTraverse()
        
        
        