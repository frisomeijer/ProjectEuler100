'''
Problem 20:
    
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

import time
start_time = time.time()

def factorial_digit_sum(n):
    factorial=1
    fact_sum=0
    for number in range(1,n+1):
        factorial*=number
    for digit in str(factorial):
        fact_sum+=int(digit)
    return fact_sum
           
print(factorial_digit_sum(100))

# calculation time: 0.0030336380004882812 seconds
print("calculation time: %s seconds" % (time.time() - start_time))   