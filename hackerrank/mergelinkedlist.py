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
    



def comparelist(llist1, llist2):
    list1 = llist1
    list2 = llist2

    while list1:
        if list1.data > list2.data:
            pass

        list1 = list1.next
        list2 = list2.next


llist1 = SinglyLinkedList()
llist1.insert_node(1)
llist1.insert_node(2)

llist2 = SinglyLinkedList()
llist2.insert_node(1)
llist2.insert_node(3)
print(comparelist(llist1.head, llist2.head))