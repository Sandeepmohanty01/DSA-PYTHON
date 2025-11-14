class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def deleteFirstNode(head):
    if head == None:
        return None
    else:
        return head.next
    
    # curr = head
    # curr.next = head.next
    # head = curr.next
    # return head

def printList(head):
    curr = head
    while curr != None:
        print(curr.data, end="->")
        curr = curr.next
    print("None")

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

printList(head)

print("------------After deletion of first Node--------------")

head = deleteFirstNode(head)

printList(head)
