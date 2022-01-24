# Python Program to Reverse an Array

import array 


def reverseArray(P):
    start = 0
    end = len(P)-1
    while start < end:
        P[start], P[end] = P[end], P[start] # Swap elements of the array while traversing to the middle
        start += 1
        end -= 1
    return P


# Enter number of elements as input
Q = int(input("\nEnter number of elements : "))

# Enter Q elements seperated by space as input
P = list(map(int,input("Enter the numbers : ").strip().split()))[:Q]

# Convert input (list) to array
P = array.array('i', P)
print("\nOriginal Array: ", P)

# Return Reversed Array
rev_P = reverseArray(P) # User-defined function to revserse array
# rev_P = array.array('i', reversed(P)) # Bulit-in function to reverse array 

print("Reversed Array: ", rev_P)

