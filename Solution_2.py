fib = [1,2]
fib_even=[2]
sum_fib_even=sum(fib_even)

while sum_fib_even<4000000:
    next_fib = fib[-2]+fib[-1]
    fib.append(next_fib)
    if next_fib%2==0:
        fib_even.append(next_fib)
        sum_fib_even=sum(fib_even)
    
print(sum_fib_even)