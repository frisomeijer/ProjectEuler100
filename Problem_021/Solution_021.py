'''
Problem 21:
    
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

import time
start_time = time.time()

def sum_proper_divisors(n):
    proper_divisors=[]
    for i in range(1,int(n/2)+1):
        if n%i==0:
            proper_divisors.append(i)
    return sum(proper_divisors)
            
def is_amicable_number(a):
    b=sum_proper_divisors(a)
    if a==sum_proper_divisors(b) and a!=b:
        return True

amicable_numbers = []
for number in range(1,10000):
    if is_amicable_number(number):
        amicable_numbers.append(number)
        
print(sum(amicable_numbers))    
# calculation time: 3.3752059936523438 seconds
print("calculation time: %s seconds" % (time.time() - start_time))   