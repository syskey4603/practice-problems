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
        return
        
        

def insertNodeAtPosition(llist, data, position):
    new_node = Node(data)
    if not llist:
        llist = new_node
        return llist
    
    cur = llist
    while cur:
        if position == 1:
            new_node.next = cur.next
            cur.next = new_node
            return llist   
        position -=1
        cur = cur.next
  
            