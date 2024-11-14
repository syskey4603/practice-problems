class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        

def reverse(llist):
    prev = None
    cur = llist
    
    while cur:
        nextnode = cur.next
        cur.next = prev
        prev = cur
        cur = nextnode
    return prev
        
        