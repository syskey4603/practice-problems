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
    prev = None
    while list1:
        if list1.data >= list2.data:

            temp = list2
            list2 = list2.next
            if not prev:
                t = llist1
                llist1 = temp
                list1 = temp
                temp.next = t
            else:
                prev.next = temp
                prev.next.next = list1
                prev = prev.next
            if not list2:
                return llist1
        else:
            prev = list1
            list1 = list1.next

    prev.next = list2
    return llist1

def printlist(head):
    cur = head
    while cur:
        print(cur.data)
        cur = cur.next




llist1 = SinglyLinkedList()
llist1.insert_node(100)


llist2 = SinglyLinkedList()

llist2.insert_node(8)
llist2.insert_node(11)
llist2.insert_node(17)
llist2.insert_node(20)
llist2.insert_node(20)
llist2.insert_node(42)
llist2.insert_node(83)
llist2.insert_node(94)
llist2.insert_node(95)
printlist(comparelist(llist1.head, llist2.head))