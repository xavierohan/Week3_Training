'''
Python program to carry out the following operations:
    1. Push the element x into the stack. (1 x)
    2. Delete the element present at the top of the stack. (2)
    3. Print the maximum element in the stack. (3)
'''

n = int(input('No. of Queries: '))
stack = []
most = []

for i in range(n):
    data = input('Enter Query: ').split(' ')
    x = int(data[0]) # Get Query index
    if len(data) > 1: 
        i = int(data[1]) # Get data to be pushed
    if x == 1:
        stack.append(i) # Push data to Stack
        if len(most)==0 or most[-1] <= i: # Track Maxelement
            most.append(i)
    elif x == 2:
        d = stack.pop() # Delete element from stack
        if most[-1] == d: 
            most.pop() # If element to be deleted is Maxelement, delete from most
    else:
        print(most[-1]) # Max element

'''

Example Output:

No. of Queries: 5
Enter Query: 1 1
Enter Query: 1 3
Enter Query: 2  
Enter Query: 1 5
Enter Query: 3
5

No. of Queries: 10
Enter Query: 1 97
Enter Query: 2
Enter Query: 1 20
Enter Query: 2
Enter Query: 1 26
Enter Query: 1 20
Enter Query: 2
Enter Query: 3
26
Enter Query: 1 91
Enter Query: 3
91

'''
