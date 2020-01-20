'''
Problem 14:
    
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

import time
start_time = time.time()

def sequence_length(n):
    sequence=[n]
    while n>1:
        if n%2 == 0:
            n /= 2
        else:
            n = 3*n + 1
        sequence.append(n)
    return len(sequence)

longest_chain=1
for i in range(500000,1000000):
    chain_length = sequence_length(i)
    if chain_length>longest_chain:
        longest_chain=chain_length
        print(i)
    
# calculation time: 23.029833793640137 seconds
print("calculation time: %s seconds" % (time.time() - start_time))   