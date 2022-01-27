'''
Python Program to get minimum average wait time for a service
'''

import heapq

cases = int(input('No. of Customers: '))
customers = []
time = 0
total_wait_time = 0
queue = []

for i in range(cases):
    customers.append ([int(x) for x in input(f"Cust{i}: (arrival_time prep_time) ").split()])
    
while customers or queue:

    while customers and (customers[0][0] <= time): 
        # if arrival time <= prep time --> populate the heap/queue
        time_index, time_prep = customers.pop(0)
        heapq.heappush(queue, (time_prep, time_index)) # Add customer to heap
        time = max(time, time_index) 

    time_prep, time_index = heapq.heappop(queue) # Get smallest prep time
    time += time_prep
    wait_time = time - time_index # Wait time = served time - arrival time 
    total_wait_time += wait_time

print("Avergae Wait Time: ", total_wait_time // cases) # avg wait time


'''

Example Output:

No. of Customers: 3
Cust0: (arrival_time prep_time) 0 3
Cust1: (arrival_time prep_time) 1 9
Cust2: (arrival_time prep_time) 2 6
Avergae Wait Time:  9

'''
