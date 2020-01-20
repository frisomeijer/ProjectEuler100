'''
Problem 15:
    
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
'''

import time
import random

#  First tried to brute force a solution by randomly navigating
def calc_routes(gridsize):
    route_list = []
    for i in range(1000000):
        route = []
        for node in range(gridsize*2):
            if route.count(1)<gridsize and route.count(2)<gridsize:
                choice = random.randint(1,2)
            elif route.count(1)<gridsize:
                choice = 1
            else:
                choice = 2
            route.append(choice)
        if route not in route_list:
            route_list.append(route)
            print(route)
    return(len(route_list))

nr_of_routes=calc_routes(7)

# This will eventually result in the solution, however the calculation time will be to long for a grid > 7x7

#%%

# Second method is a probabilistic approach
start_time = time.time()

def calc_paths(gridsize):
    total_arrangements=1
    arrangements_per_route=1
    for step in range(1,gridsize*2+1):
        total_arrangements *= step    
    for step in range(1,gridsize+1):        
        arrangements_per_route *= step**2     
    return total_arrangements/arrangements_per_route

print(calc_paths(20))
# calculation time: 0.0012271404266357422 seconds
print("calculation time: %s seconds" % (time.time() - start_time))   