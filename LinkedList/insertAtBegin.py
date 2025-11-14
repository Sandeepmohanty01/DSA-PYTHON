class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def inserAtBeginning(head,data):
    temp = Node(data)
    temp.next = head
    return temp

def printList(head):
    curr = head
    while curr != None:
        print(curr.data, end="->")
        curr = curr.next
    print("None")

head = None
head = inserAtBeginning(head,10)
head = inserAtBeginning(head,20)
head = inserAtBeginning(head,30)


printList(head)

        