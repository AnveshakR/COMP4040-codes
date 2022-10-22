# In a BST, we have for any node x in the tree, the key of every node in the left subtree of x is less than or equal to the key of x, 
# and the key of every node in the right subtree of x is strictly greater than the key of x. 
# This definition, however, makes it impossible to balance a BST for multiple items with the same key. 
# For example, if you have 10 items of the same key, then the BST is a stright line and there is no way to balance it. 
# Thus, in any balanced binary search tree, would assume that keys are distinct. 
# To handle multiple items with the same key, we can simply place these items in one node by maintaining a list of these items for that node.
# Modify AVL tree implementation given in class to handle this situation on inputs of the following form: (key, ID), 
# where different IDs may have the same key.

import random

class treeNode(object):
    def __init__(self, value, data):
        self.value = value # key value
        self.ID = [] # adding a an array called ID which will store the corresponding data for a given key value
        self.ID.append(data)
        self.l = None
        self.r = None
        self.h = 1

class AVLTree(object):

    def insert(self, root, key, data):
    
        if not root:
            return treeNode(key, data)
        elif key == root.value: # if the key is equal to the current value
            root.ID.append(data) # append the key's data to the existing key's ID array
        elif key < root.value:
            root.l = self.insert(root.l, key, data)
        else:
            root.r = self.insert(root.r, key, data)

        root.h = 1 + max(self.getHeight(root.l), self.getHeight(root.r))

        b = self.getBal(root) # get balance factor of current tree and check for values {-1,0,1}

        if b > 1 and key < root.l.value: # if >1 and on left side
            return self.rRotate(root) # perform R rotation

        if b < -1 and key > root.r.value: # if <-1 and on right side
            return self.lRotate(root) # perform L rotation

        if b > 1 and key > root.l.value: # if >1 and on right side
            root.l = self.lRotate(root.l) # perform LR rotation
            return self.rRotate(root)

        if b < -1 and key < root.r.value: # if <-1 and on left side
            root.r = self.rRotate(root.r) # perform RL rotation
            return self.lRotate(root)

        return root

    def lRotate(self, z): # L rotation

        y = z.r
        T2 = y.l

        y.l = z
        z.r = T2

        z.h = 1 + max(self.getHeight(z.l), self.getHeight(z.r))
        y.h = 1 + max(self.getHeight(y.l), self.getHeight(y.r))

        return y

    def rRotate(self, z): # R rotation

        y = z.l
        T3 = y.r

        y.r = z
        z.l = T3

        z.h = 1 + max(self.getHeight(z.l), self.getHeight(z.r))
        y.h = 1 + max(self.getHeight(y.l), self.getHeight(y.r))

        return y

    def getHeight(self, root):
        if not root:
            return 0

        return root.h

    def getBal(self, root):
        if not root:
            return 0

        return self.getHeight(root.l) - self.getHeight(root.r)

    def preOrder(self, root):
        if not root:
            return

        print("{0}".format(root.value), end='')
        print("{0}".format(root.ID), end=', ')
        self.preOrder(root.l)
        self.preOrder(root.r)
    
    def inOrder(self, root):
        if not root:
            return
        
        self.inOrder(root.l)
        print("{}".format(root.value), end='')
        print("{}".format(root.ID), end=", ")
        self.inOrder(root.r)
        
    def postOrder(self, root):
        if not root:
            return
        
        self.inOrder(root.l)
        self.inOrder(root.r)
        print("{}".format(root.value), end='')
        print("{}".format(root.ID), end=', ')

# driver's code
def driver(key, ID):

    print("key values: ", key)
    print("data values: ", ID)

    Tree = AVLTree()
    root = None

    for i in range(len(key)): # inserting into AVL tree
        root = Tree.insert(root, key[i], ID[i])

    # Preorder Traversal
    print("Preorder traversal")
    Tree.preOrder(root)
    print()

    # Inorder Traversal
    print("Inorder traversal")
    Tree.inOrder(root)
    print()

    # Postorder Traversal
    print("Postorder traversal")
    Tree.postOrder(root)
    print()

def main():
    
    print("for random values")
    n = 10 # for 'n' (key, ID) pairs
    key = [random.randrange(1,10) for _ in range(n)] # 'n' keys from 1,10
    data = [random.randrange(1,100) for _ in range(n)] # 'n' data from 1,100
    driver(key, data)

    print("\n\n")

    print("for custom values")
    key = list(map(int, input("enter key values separated by commas: ").strip().split(',')))
    data = list(map(int, input("enter data values separated by commas: ").strip().split(',')))
    if (len(key) != len(data)):
        print("key and data have unequal lengths, try again")
        exit(1)
    driver(key, data)

if __name__ == '__main__':
    main()