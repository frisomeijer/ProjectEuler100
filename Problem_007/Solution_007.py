'''
Problem 7:
    
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''    

import time
import math

start_time = time.time()

def check_prime(n):
    for i in range(2, math.ceil(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def nth_prime(n):
    prime_index=1
    possible_prime=1
    while prime_index<n:
        possible_prime+=2    
        prime = check_prime(possible_prime)        
        if prime:
            prime_index+=1
            if prime_index==n:
                print("%sth prime: %s" % (prime_index,possible_prime))
                return prime
    
nth_prime(10001)

# calculation time: 0.16196155548095703 seconds
print("calculation time: %s seconds" % (time.time() - start_time))           