class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printList(head):
    curr = head
    while curr != None:
        print(curr.data)
        curr = curr.next
    print()


def middleOfList(head):
    if head == None:
        return None
    
    count = 0

    curr = head

    while curr:
        curr = curr.next
        count += 1

    curr = head

    for i in range(count//2):
        curr = curr.next
    print(curr.data)

    
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

printList(head)
middleOfList(head)

        
    
