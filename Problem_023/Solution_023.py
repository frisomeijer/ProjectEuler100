'''
Problem 23:
'''
import math
import time
start_time = time.time()

def sum_proper_divisors(n):
    divisor_list=[]
    for i in range(1,math.floor(math.sqrt(n))+1):
        if n%i==0:
            divisor_list.append(i)
            if i**2 != n and i != 1:
                divisor_list.append(n/i)          
    return sum(divisor_list)
    
def is_abundant(n):
    if sum_proper_divisors(n)>n:
        return True
    else:
        return False

def can_be_written_as_sum(a):
    for b in abundant_number_list:
        if b<a:
            difference=a-b
            if is_abundant(difference):
                return True
        else:
            break

abundant_number_list =[] 
for number in range(28124):
    if is_abundant(number) and number not in abundant_number_list:
        abundant_number_list.append(number)
      
positive_integer_list = []            
for i in range(28124):
   if not can_be_written_as_sum(i):
       positive_integer_list.append(i)

print(sum(positive_integer_list))
    
# calculation time: 39.68510103225708 seconds
print("calculation time: %s seconds" % (time.time() - start_time))   