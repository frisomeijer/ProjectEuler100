'''
Problem 5:
    
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

import time

start_time = time.time()

def smallest_evenly_divisible_number(n):
# Finds the smallest evenly divisible number by al numbers from 1 to n.
    for num in range(n,1000000000,n):
        for j in range(1,n+1):
            mod = num%j
            if mod != 0:
                break
            if j==n:
                return num
    
print("smallest evenly divisble number: %s" % smallest_evenly_divisible_number(20))

# calculation time: 26.867398500442505 seconds
print("calculation time: %s seconds" % (time.time() - start_time))           