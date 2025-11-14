class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def searchItem(head, x):
    curr = head
    i = 1
    while curr != None:
        if curr.data == x:
            return  i
        curr = curr.next
        i = i+1
    return -1


def printList(head):
    curr = head
    while curr != None:
        print(curr.data, end="->")
        curr = curr.next
    print("None")
    

head = Node(10)
# head = Node(10)
# head.next = Node(20)
# head.next.next = Node(40)
# head.next.next.next = Node(30)
printList(head)
print(searchItem(head,10))