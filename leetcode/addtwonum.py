
class Solution:
    def addTwoNumbers(l1, l2):
        l1str = ""
        l2str = ""
        litotal = []
        for x in reversed(l1):
            l1str += str(x)

        for y in reversed(l2):
            l2str += str(y)
        
        l1int = int(l1str)
        l2int = int(l2str)

        total = l2int + l1int

        for item in reversed(str(total)):
            litotal.append(int(item))

        return litotal




tests = [
    (
        (["addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"],
         [[1], [3], [1, 2], [1], [1], [1]],),
        [None, None, None, 2, None, 3],
    ),
    (
        (["addAtHead", "addAtHead", "addAtHead", "addAtIndex", "deleteAtIndex", "addAtHead", "addAtTail", "get", "addAtHead", "addAtIndex", "addAtHead"],
         [[7], [2], [1], [3, 0], [2], [6], [4], [4], [4], [5, 0], [6]],),
        [None, None, None, None, None, None, None, 4, None, None, None],
    ),
    (
        (["addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"],
         [[1], [3], [1, 2], [1], [0], [0]],),
        [None, None, None, 2, None, 2],
    ),
    (
        (["addAtIndex", "addAtIndex", "addAtIndex", "get"],
         [[0, 10], [0, 20], [1, 30], [0]],),
        [None, None, None, 20],
    ),
]