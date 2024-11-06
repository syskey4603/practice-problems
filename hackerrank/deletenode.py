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
    
    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
        
    def delete_node(self, pos):
        posval = 0
        cur = self.head
        tempcur = None
        if pos == 0:
            self.head = cur.next
            return
        while cur:
            if posval == pos:
                tempcur.next = cur.next
                return
            posval+=1
            tempcur = cur
            cur = cur.next

        

newlist = SinglyLinkedList()

newlist.insert_node(11)
newlist.insert_node(12)
newlist.insert_node(8)
newlist.insert_node(18)
newlist.insert_node(16)
newlist.insert_node(5)
newlist.insert_node(18)
newlist.delete_node(0)

newlist.print_list()

7
11
12
8
18
16
5
18
0