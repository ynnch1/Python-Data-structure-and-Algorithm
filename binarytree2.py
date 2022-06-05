# Python program to introduce Binary Tree

# A class that represents an individual node in a
# Binary Tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# A function to do inorder tree traversal
def printInorder(root):  # left, root, right
    if root:
        # First recur on left child
        printInorder(root.left)
        # then print the data of node
        print(root.val),
        # now recur on right child
        printInorder(root.right)


# A function to do postorder tree traversal
def printPostorder(root):  # left, right, root
    if root:
        # First recur on left child
        printPostorder(root.left)
        # the recur on right child
        printPostorder(root.right)
        # now print the data of node
        print(root.val),


# A function to do preorder tree traversal
def printPreorder(root):  # root, left, right
    if root:
        # First print the data of node
        print(root.val),
        # Then recur on left child
        printPreorder(root.left)
        # Finally recur on right child
        printPreorder(root.right)

def abc():
    if 


root = Node('D')

root.left = Node('B')
root.left.left = Node('A')
root.left.right = Node('C')

root.right = Node('F')
root.right.left = Node('E')
root.right.right = Node('G')


print("Preorder traversal of binary tree is")
printPreorder(root)

print("\nInorder traversal of binary tree is")
printInorder(root)

print("\nPostorder traversal of binary tree is")
printPostorder(root) 