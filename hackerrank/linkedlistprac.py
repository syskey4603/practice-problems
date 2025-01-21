class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_node(self, data):
        newnode = Node(data)
        if not self.head:
            self.head = newnode
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = newnode

    def printlist(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

linkedlist = SinglyLinkedList()
linkedlist.insert_node(4)
linkedlist.insert_node(3)
linkedlist.insert_node(2)
linkedlist.insert_node(1)

linkedlist.printlist()

#testing