# Python Program to Print Elements of Linked List


# Node class
class Node:
 
    # Initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as None
 
 
# SinglyLinkedList class
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


a = []
p = int(input("\nNo. of elements: "))
for i in range(p):
    a.append(int(input(f"Enter element{i}: ")))

ll = SinglyLinkedList()

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


'''

Example Output:

No. of elements: 5
Enter element0: 1
Enter element1: 22
Enter element2: 30
Enter element3: 2
Enter element4: 5
1
22
30
2
5

'''