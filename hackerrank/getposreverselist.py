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
        

def reverselist(head):
    cur = head
    prev = None
    newhead = None
    while cur:
        temp = cur.next
        newhead = cur
        newhead.next = prev
        prev = cur
        cur = temp


    return newhead

def getpos(head, pos):
    cur = head
    index = 0
    while index != pos:
        index+=1
        cur=cur.next
    return cur




newlist = SinglyLinkedList()
newlist.insert_node(5)
newlist.insert_node(4)
newlist.insert_node(3)
newlist.insert_node(2)
newlist.insert_node(1)

print(getpos(reverselist(newlist.head), 2))