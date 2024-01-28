class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def show(self):

        while node is not None:
            print(node.value)
            node = node.next

llist = LinkedList()
head = Node("Head Node")
llist.head = head
llist.show
      