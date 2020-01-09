'''
Problem 9:
    
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

import time
import math
start_time = time.time()

def pythagorean_triplet_product(n):
    # Calculates the product abc of a Pythagorean triplet
    # for wich the sum a+b+c = n and a<b<c
    for c in range(math.floor(n/3),n):
        for b in range(1,c):
            for a in range(1,b):
                if a+b+c==n and a**2+b**2==c**2:
                    return a*b*c

product_abc = pythagorean_triplet_product(1000)
print(product_abc)

# calculation time: 0.712416410446167 seconds
print("calculation time: %s seconds" % (time.time() - start_time))   
    