import time
start_time = time.time()

def sum_square_difference(n):
# Finds the difference between the sum of the squares 
# of the first n natural numbers and the square of the sum.
    sum_sqaures = sum([x**2 for x in range(n+1)])
    square_sum = sum([x for x in range(n+1)])**2
    return square_sum - sum_sqaures
    
print("sum square difference: %s" % sum_square_difference(100))
print("calculation time: %s seconds" % (time.time() - start_time))           