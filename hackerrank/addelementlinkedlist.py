class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        

def insertNodeAtTail(head, data):
    new_node = Node(data)
    if not head:
        head = new_node
        return head
    last = head
    while last.next:
        last = last.next
    last.next = new_node
    return head

def print_singly_linked_list(head):
    cur = head
    while cur:
        print(cur.data)
        cur = cur.next
    return


if __name__ == '__main__':

    llist_count = int(input())

    llist = SinglyLinkedList()

    for i in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head)