class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
class DoublyLinkedList:
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
        new_node.prev = last
    
    def print_list(self):
        # Print the list in forward order
        current = self.head
        while current:
            print(current.data, end=" -> " if current.next else "\n")
            current = current.next

def sortedInsert(head, data):
    cur = head
    newnode = Node(data)
    
    if cur is None:
        return newnode
    
    if data < cur.data:
        newnode.next = cur
        cur.prev = newnode
        return newnode
    
    while cur.next and cur.data < data:
        cur = cur.next
    
    if cur.data > data:
        oldprev = cur.prev
        cur.prev = newnode
        newnode.next = cur
        if oldprev:
            oldprev.next = newnode
            newnode.prev = oldprev
    else:
        cur.next = newnode
        newnode.prev = cur
    
    return head

# Test Case 5
numbers = [
    7, 7, 8, 28, 32, 33, 39, 48, 48, 53, 55, 62, 64, 66, 68, 68,
    76, 81, 87, 88, 90, 91, 92, 94, 94
]
value_to_insert = 95

# Create the doubly linked list
dll = DoublyLinkedList()
for number in numbers:
    dll.insert_node(number)

# Insert the value into the sorted linked list
dll.head = sortedInsert(dll.head, value_to_insert)

# Print the resulting linked list
print("Linked List after insertion:")
dll.print_list()
