'''
Problem 22:
'''

import time
start_time = time.time()

alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
            'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def alphabetic_value(name):
    alphabetic_value=0
    for letter in name:
        alphabetic_value+=alphabet.index(letter)+1
    return alphabetic_value    


names = open("names.txt","r").read().replace('"','').split(',')
names.sort()

score=0
for name in names:
    score+=alphabetic_value(name)*(names.index(name)+1)

    
# calculation time: 3.3752059936523438 seconds
print("calculation time: %s seconds" % (time.time() - start_time))   