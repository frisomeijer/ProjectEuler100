'''
Problem 10:
    
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''

import time
import math

start_time = time.time()

def check_prime(n):
    for i in range(2, math.ceil(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def prime_sum(n):
    prime_sum=2
    for i in range(3,n,2):
        prime =check_prime(i)
        if prime:
            prime_sum+=i
    return prime_sum

print(prime_sum(2000000))
    
# calculation time: 10.357031345367432 seconds
print("calculation time: %s seconds" % (time.time() - start_time))   
    