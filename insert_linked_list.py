# create new node class to define node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# create linked list class which contain its behavior such push, append, pirnt out the linked list data


class LinkedList:
    def __init__(self):
        self.head = None
# make the new node as the head

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print('The given previous node must be in linked list')
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return

            last = self.head
            while(last, next):
                last = last.next
            last.next = mew_mode

    # Returns data at given index in linked list
    def getNth(self, index):
        current = self.head  # Initialise temp
        count = 0  # Index of current node
        # Loop while end of linked list is not reached
        while (current):
            if (count == index):
                return current.data
            count += 1
            current = current.next
        # if we get to this line, the caller was asking
        # for a non-existent element so we assert fail
        return 0

    # Counts the no . of occurrences of a node
    # (search_for) in a linked list (head)
    def count(self, search_for):
        current = self.head
        count = 0
        while(current is not None):
            if current.data == search_for:
                count += 1
            current = current.next
        return count

    # print
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next


# code execution
if __name__ == '__main__':
    llist = LinkedList()
    llist.append(6)
    llist.push(7)
    llist.push(1)
    llist.insertAfter(llist.head.next, 8)

    llist.printList()
