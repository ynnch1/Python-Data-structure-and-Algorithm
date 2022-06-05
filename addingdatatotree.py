#Python program to introduce Binary tree

#A class that represents an individual node in a binary tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

#create root
root = Node(1)
''' following is the tree after the above statement
        1
    / \
    None None'''

root.left = Node(2)
root.right = Node(3)

''' 2 and 3 become left and right children of 1
        1
        / \
        2   3
    / \ / \ None None None None'''

root.left.left = Node(4)
''' 4 becomes left child of 2
        1
    /   \
    2       3
    / \ / \
4 None None None
/ \
None None'''