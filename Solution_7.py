import time
import math

start_time = time.time()

def check_prime(n):
    for i in range(3, math.ceil(math.sqrt(n)), 2):
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
print("calculation time: %s seconds" % (time.time() - start_time))           