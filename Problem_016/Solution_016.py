'''
Problem 16:
    
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''

import time
start_time = time.time()

def sum_of_digits(n):
    string_of_number = str(n)
    sum_of_digits=0
    for digit in string_of_number:
        sum_of_digits += int(digit)          
    return sum_of_digits

print(sum_of_digits(2**1000))

# calculation time: 0.0 seconds
print("calculation time: %s seconds" % (time.time() - start_time))   