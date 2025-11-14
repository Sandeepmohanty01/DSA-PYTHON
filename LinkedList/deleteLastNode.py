class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def deleteLastNode(head):

# handle the corner case
    if head == None:
        return None    
    if head.next == None:
        return None
    
    curr = head
   
    while curr.next.next != None:
        curr = curr.next
    curr.next = None  
    return head

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

print("------------After deletion of Last Node--------------")

head = deleteLastNode(head)

printList(head)