class Node:
    def __init__ (self, value):
        self.left = None
        self.right = None
        self.value = value

class Tree:
    def __init__ (self):
        self.root = None

    def isEmpty (self):
        if (self.root == None):
            return True
        else:
            return False


    ##Add operation

    def add (self, value):
        if (self.root == None):
            self.root = Node(value)
        else:
            self._add (value, self.root)

    def _add (self, value, node):
        if (value < node.value):
            if (node.left != None):
                self._add(value, node.left)
            else:
                node.left = Node (value)
        else:
            if (node.right != None):
                self._add (value, node.right)
            else:
                node.right = Node (value)
                
    ##Delete operation
    def delete (self, value):
        self._delete (value, self.root)

    def _delete (self, value, node):
        if (node == None):
            return node
        if (node.value < value):
            node.left = self._delete (value, node.left)
            
        elif (node.value > value):
            node.right = self._delete (value, node.right)
            
        elif (node.left != None and node.right != None):
            node.value = self.findMin (node.right).value
            node.right = self._delete (node.value, node.right)
        else:
            if (node.left != None):
                node = node.left
            else:
                node = node.right
        return node
    

    
    ##Search Min Operation
    def _findMin (self, node):
        if (node == None):
            return None
        elif (node.left == None):
            return node
        else:
            return self._findMin(node.left)
        
    ##Search Max Operation   
    def findMin (self):
        if (self.isEmpty()):
            return None
        else:
            return (self._findMin(self.root)).value

    def _findMax (self, node):
        if (node == None):
            return None
        elif (node.right == None):
            return node
        else:
            return self._findMax(node.right)
        
    def findMax (self):
        if (self.isEmpty()):
            return None
        else:
            return (self._findMax(self.root)).value
    
    
    #####Print Operations

    #Preorder
    def printTreePreOrder (self):
        if (self.isEmpty):
            self._printTreePreOrder (self.root)

    def _printTreePreOrder(self, node):
        if (node != None):
            print(node.value)
            self._printTreePreOrder (node.left)
            self._printTreePreOrder (node.right)
    #Inorder

    def printTreeInOrder (self):
        if (self.isEmpty):
            self._printTreeInOrder (self.root)

    def _printTreeInOrder (self, node):
        if (node != None):
            self._printTreeInOrder (node.left)
            print (node.value)
            self._printTreeInOrder (node.right)
    #Postorder

    def printTreePostOrder (self):
        if (self.isEmpty):
            self._printTreePostOrder (self.root)

    def _printTreePostOrder (self, node):
        if (node != None):
            self._printTreePostOrder (node.left)
            self._printTreePostOrder (node.right)
            print (node.value)
         

tree = Tree ()
tree.add(7)
tree.add(4)
tree.add(10)
tree.add(8)
tree.add(2)
tree.add(1)
tree.add(5)
tree.delete(5)
tree.printTreePostOrder()

print ("El valor mínimo es: "+ str(tree.findMin()))
print ("El valor máximo es: "+ str(tree.findMax()))
        
