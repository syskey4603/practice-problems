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
        

    def reversePrint(self):
        prev = None
        cur = self.head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev
            

    def printall(self, head):
        cur = head
        while cur:
            print(cur.data)
            cur = cur.next



newlist = SinglyLinkedList()
newlist.insert_node(1)
newlist.insert_node(2)
newlist.insert_node(3)

head = newlist.reversePrint()

'''

first element should point to none
the rest of them should just point to the previous element

'''