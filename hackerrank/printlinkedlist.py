class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
        return


testlinkedlist = LinkedList()
testlinkedlist.append(5)
testlinkedlist.append(6)
testlinkedlist.append(7)
testlinkedlist.append(8)

testlinkedlist.display()