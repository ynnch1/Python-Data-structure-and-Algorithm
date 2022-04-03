# create new node class to define node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# create linked list class which contain its behavior such push, append, pirnt out the linked list data
class LinkedList:
    def __init__(self):
        self.head = None
#make the new node as the head
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
#
    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node 
            return

            last = self.head
            while(last, next):
                last = last.next
            last.next = mew_mode
#print
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
#code execution
if __name__ == '__main__':
    llist = LinkedList()
    llist.append(6)
    llist.push(7)
    llist.push(1)

    llist.printList()