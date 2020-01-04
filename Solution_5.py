import numpy as np

def smallest_evenly_divisible_number(n):
# Finds the smallest evenly divisible number by al numbers from 1 to n.
    for num in np.arange(n,1000000000,n):
        for j in range(1,n+1):
            mod = num%j
            if mod != 0:
                break
            if j==n:
                return num
                
print(smallest_evenly_divisible_number(20))