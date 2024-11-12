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
        return
    
    def printinreverse(self):
        templast = None
        while self.head:
            t = self.head.next
            self.head.next = templast
            templast = self.head
            self.head = t
        self.head = templast
            




        
    def printlist(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next



def findlast(head):
    if not head:
        return None
    last = head
    while last.next:
        last = last.next
    return last

def findsecondlast(head):
    if not head:
        return None
    secondlast = head
    last = findlast(head)
    while secondlast.next != last:
        secondlast = secondlast.next
    return secondlast
        
newlist = SinglyLinkedList()

newlist.insert_node(1)
newlist.insert_node(2)
newlist.insert_node(3)
newlist.printinreverse()
newlist.printlist()


'''
set the new first element to the next one
make the first element point to none
the next element points to that one

repeat

''' 