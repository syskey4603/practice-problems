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
        

def removeDuplicates(llist):
    cur = llist
    uniquelist = []
    while cur:
        if cur.data not in uniquelist:
            uniquelist.append(cur.data)
        cur = cur.next
    newlist = SinglyLinkedList()
    curnew = newlist.head
    for x in uniquelist:
        if not newlist.head:
            newlist.head = Node(x)
            curnew = newlist.head
            continue
        curnew.next = Node(x)
        curnew = curnew.next
    return newlist.head
        


        

newlist = SinglyLinkedList()
newlist.insert_node(1)
newlist.insert_node(1)
newlist.insert_node(1)
newlist.insert_node(2)
newlist.insert_node(2)
newlist.insert_node(3)
newlist.insert_node(4)

print(removeDuplicates(newlist.head))