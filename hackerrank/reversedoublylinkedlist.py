class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
class DoublyLinkedList:
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
        new_node.prev = last

def reverselist(head):
    last = head
    while last.next:
        last=last.next
    newlist = DoublyLinkedList()
    while last:
        print(last.data)
        newlist.insert_node(last.data)
        last = last.prev
    return newlist.head


newlist = DoublyLinkedList()
newlist.insert_node(1)
newlist.insert_node(2)
newlist.insert_node(3)
print(reverselist(newlist.head))