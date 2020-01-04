palindromic_numbers = []

for i in range(1000):
    for j in range(1000):
        product = i * j
        digits = (len(str(product)))
        if digits%2==0 and str(product)[:int(digits/2)]==str(product)[:int(digits/2)-1:-1]:
            palindromic_numbers.append(product)
            
print(max(palindromic_numbers))