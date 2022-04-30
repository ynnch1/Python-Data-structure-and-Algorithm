


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
    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print('The given previous node must be in linked list')
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
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
    def deleteNode(self, key):
        temp = self.head
        if(temp is not None):
            if(temp.data == key):
                self.head = temp.next
                temp = None
                return

        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if(temp == None):
            return
        prev.next = temp.next
        temp = None 
    #Delete by position
    def deletePostionNode(self, position):
        if self.head is None:
            return
        if position == 0:
            self.head = self.head.next
            return self.head
        index = 0
        current = self.head
        prev = self.head
        temp = self.head
        while current is not None:
            if index == position:
                temp = current.next
                break
            prev = current
            current = current.next
            index += 1
        prev.next = temp
        return prev
    
    def getCount(self):
        temp = self.head
        count = 0
        while(temp):
            count += 1
            temp = temp.next
        return count 
    
    def search(self, x):
        current = self.head
        while current != None:
            if current.data == x:
                return True
            current = current.next
        return False 

    #print
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
#code execution
if __name__ == '__main__':
    llist = LinkedList()


    # 1
    print("1. create new linked list")
    # your code here and bellow
    llist.append(5)
    llist.push(4)
    llist.push(8)
    llist.push(9)

    llist.printList() # print out the #1 expect output
    print('\n')

    print(llist.getCount())
    print('\n')

    llist.deleteNode(4)
    llist.printList()
    print('\n')

    llist.deletePostionNode(0)
    llist.printList()
    print('\n')

    print(llist.search(9))

    data = 8

    if llist.search(data):
        print('There is the number ' + str(data) + ' in the list')
    else:
        print('The number ' + str(data) + ' is not in the list')


 #  llist.printList()