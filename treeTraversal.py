#Python program for tree traversal
#A class that represents an individual node in a binary tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

#A function to do inorder tree traversal
def printInorder(root): #left, root, right
    if root:
        #First recur on left child
        printInorder(root.left)
        #then print the data of the node
        print(root.val)
        #now recur on the right child
        printInorder(root.right)

#A function to do postoder tree traversal
def printPostorder(root): #left, right, root
    if root:
        #first recur on left child
        printPostorder(root.left)
        #then recur on right child
        printPostorder(root.right)
        #now print the data of node
        print(root.val),

#A function to do preorder tree traversal
def printPreorder(root): #root, left, right
    if root:
        #First print the data of node
        print(root.val),
        #then recur on left child
        printPreorder(root.left)
        #finally recur on right child
        printPreorder(root.right)

#Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Preorder traversal of binary is")
printPreorder(root)

print("\nInorder traversal of binary tree is")
printInorder(root)

print("\nPostorder traversal of binary tree is")
printPostorder(root)