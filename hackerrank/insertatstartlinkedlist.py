class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    


def insertNodeAtHead(llist, data):
    new_node = Node(data)
    if not llist:
        llist = new_node
        return llist
    previous = llist
    llist = new_node
    new_node.next = previous
    return llist

def print_singly_linked_list(head):
    cur = head
    while cur:
        print(cur.data)
        cur = cur.next
    

if __name__ == '__main__':

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtHead(llist.head, llist_item)
        llist.head = llist_head
    
    print_singly_linked_list(llist.head)