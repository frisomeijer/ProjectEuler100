'''
Problem 3:
    
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

import time

start_time = time.time()

composite = 600851475143

def check_prime(number):
# This function checks if the input number is a prime number for number>2
    for num in range(2,number):
        if number%num==0:
            break
        if num==number-1:
            return number
        
# Calculate prime numbers up to 10000
prime_list = [2]
for i in range(2,10000):
    prime = check_prime(i)
    if prime:
        prime_list.append(prime)    

# Calculate prime factors
prime_factors = []
while composite >=2:
    for prime in prime_list:
        composite_quotient = composite/prime
        if composite_quotient%1==0:
            composite = composite_quotient
            prime_factors.append(prime)

# Calcualte maximum prime factor            
max_prime_factor = max(prime_factors)
print(max_prime_factor)            

# calculation time: 0.6089754104614258 seconds
print("calculation time: %s seconds" % (time.time() - start_time))   