# Python program with LinkedList Functions


class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.head = None

    def printLinkedList(self):
        temp = self.head 
        while (temp):
            print(temp.data)
            temp = temp.next # Go to next element in LinkedList

    # inserting the node at the beginning
    def insertAtStart(self, data):
        if self.head == None:
            newNode = Node(data)
            self.head = newNode
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode

    # inserting the node in between
    def insertBetween(self, previousNode, data):
        if (previousNode.next is None):
            print('Previous node should have next node!')
        else:
            newNode = Node(data)
            newNode.next = previousNode.next
            previousNode.next = newNode

    # inserting at the end 
    def insertAtEnd(self, data):
        newNode = Node(data)
        temp = self.head
        while(temp.next != None):
            temp = temp.next
        temp.next = newNode

    # iterative search
    def search(self, node, data):
        if node == None:
            return False
        if node.data == data:
            return True
        node = node.next
        return self.search(node, data)


ll = LinkedList()
ll.head = Node(10)               
node2 = Node(20)
ll.head.next = node2         
node3 = Node(30)
node2.next  = node3              
ll.insertAtStart(40)            
ll.insertBetween(node2, 50)       
ll.insertAtEnd(60)
ll.printLinkedList()
x = 10
print(f"Search for {x} in linkedlist: ", ll.search(ll.head, x))

'''

Example Output:

40
10
20
50
30
60
Search for 10 in linkedlist:  True

'''