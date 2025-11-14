class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertAtAnyPosition(head, data, pos):
    temp = Node(data)
    if pos == 1:
        temp.next = head
        return temp
    curr = head

    for i in range(pos-2):
        curr = curr.next
        if curr == None:
            return head
    temp.next = curr.next
    curr.next = temp
    return head

def PrintList(head):
    curr = head    
    while curr != None:
        print(curr.data, end="->")
        curr = curr.next        
    print("None")

head = Node(13)
head.next = Node(14)
head.next.next= Node(54)
head.next.next.next = Node(43)
insertAtAnyPosition(head, 20, 2)
PrintList(head)
