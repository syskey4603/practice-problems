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
    
newlist = SinglyLinkedList()
newlist.insert_node(1)
newlist.insert_node(2)
newlist.insert_node(3)

last = newlist.head
while last.next:
    last = last.next
last.next = newlist.head


def isCycle(head):
    cyclelist = []
    cur = head
    while cur.next:
        if cur in cyclelist:
            return 1
        cyclelist.append(cur)
        cur = cur.next
    return 0    
    


print(isCycle(newlist.head))

"""cur = newlist.head
while cur.next:
    print(cur.data)
    cur = cur.next"""