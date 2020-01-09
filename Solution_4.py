'''
Problem 4:
    
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
import time

start_time = time.time()

palindromic_numbers = []

for i in range(1000):
    for j in range(1000):
        product = i * j
        digits = (len(str(product)))
        if digits%2==0 and str(product)[:int(digits/2)]==str(product)[:int(digits/2)-1:-1]:
            palindromic_numbers.append(product)
            
print(max(palindromic_numbers))

# calculation time: 1.2189786434173584 seconds
print("calculation time: %s seconds" % (time.time() - start_time))        