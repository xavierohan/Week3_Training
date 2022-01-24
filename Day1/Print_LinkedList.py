# Python Program to Print Elements of Linked List


# Node class
class Node:
 
    # Initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as NULL
 
 
# Linked List class contains a Node object
class SinglyLinkedList:
 
    # Initialize head
    def __init__(self):
        self.head = None

# Traverse and Print elements of LinkedList
def printLinkedList(ll):
    temp = ll.head # Start traversal from head
    while (temp):
        print(temp.data)
        temp = temp.next # Go to next element in LinkedList


ll = SinglyLinkedList()
a = list(input("Enter data : ").strip().split())

# Initialize Head
if len(a)!=0:
    node = Node(a[0])
    ll.head = node
else:
    raise Exception("No input provided / List is Empty")

# Add Remaining Nodes
for val in a[1:]:
    node.next = Node(val)
    node = node.next 

# Print elements of LinkedList
printLinkedList(ll)