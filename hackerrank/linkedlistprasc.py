class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

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
        return
    def displaylinkedlist(self):
        cur = self.head
        while cur:
            cur = cur.next
        print(cur)

linkedlist = SinglyLinkedList()
linkedlist.insert_node(Node(4))

linkedlist.displaylinkedlist()