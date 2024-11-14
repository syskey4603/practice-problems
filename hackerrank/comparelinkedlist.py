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
    

def comparelists(llist1, llist2):
    list1 = llist1
    list2 = llist2

    while list1 and list2:

        if list1.data != list2.data:
            return False


        list1 = list1.next
        list2 = list2.next

    if list1 or list2:
        return False
    return True


list1 = SinglyLinkedList()
list1.insert_node(1)
list1.insert_node(2)
list1.insert_node(3)
list1.insert_node(4)

list2 = SinglyLinkedList()
list2.insert_node(1)
list2.insert_node(2)
list2.insert_node(3)
list2.insert_node(4)

print(comparelists(list1.head, list2.head))