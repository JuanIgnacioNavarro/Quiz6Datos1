
class Node:
    def __init__ (self, value):
        self.left = None
        self.right = None
        self.value = value

class Tree:
    #Global atributes for tests
    resultPostOrder = ""
    resultPreOrder = ""
    resultInOrder = ""
    
    #Initial Method
    def __init__ (self):
        self.root = None
    #Verify if the tree is empty
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
        if (value < node.value):
            node.left = self._delete (value, node.left)
            
        elif (value > node.value):
            node.right = self._delete (value, node.right)
            
        elif (node.left != None and node.right != None):
            node.value = self._findMin (node.right).value
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
            self.resultPreOrder=""
            self._printTreePreOrder (self.root)
        return self.resultPreOrder

    def _printTreePreOrder(self, node):
        if (node != None):
            print(node.value)
            self.resultPreOrder+= str(node.value) +  " "
            self._printTreePreOrder (node.left)
            self._printTreePreOrder (node.right)
            
    #Inorder

    def printTreeInOrder (self):
        if (self.isEmpty):
            self.resultInOrder=""
            self._printTreeInOrder (self.root)
        return self.resultInOrder

    def _printTreeInOrder (self, node):
        if (node != None):
            self._printTreeInOrder (node.left)
            print (node.value)
            self.resultInOrder+= str(node.value) +  " "
            self._printTreeInOrder (node.right)
            
    #Postorder

    def printTreePostOrder (self):
        if (self.isEmpty):
            self.resultPostOrder=""
            self._printTreePostOrder (self.root)
        return self.resultPostOrder

    def _printTreePostOrder (self, node):
        if (node != None):
            self._printTreePostOrder (node.left)
            self._printTreePostOrder (node.right)
            print (node.value)
            self.resultPostOrder+= str(node.value) +  " "
            
       
         
tree = Tree ()
tree.add(7)
tree.add(4)
tree.add(10)
tree.add(2)
tree.add(1)
tree.add(5)

print ("Print PostOrder: ")
tree.printTreePostOrder()
print ("Print PreOrder: ")
tree.printTreePreOrder()
print ("Print InOrder: ")
tree.printTreeInOrder()

print ("El valor mínimo es: "+ str(tree.findMin()))
print ("El valor máximo es: "+ str(tree.findMax()))
print (tree.printTreePreOrder())

        
