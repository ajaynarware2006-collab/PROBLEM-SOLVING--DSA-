def sumBase(n, k):
    sum=0
    while n > 0:
        x = n % k
        sum += x
        n = n // k
    
    return sum

print(sumBase(34,6))
print(sumBase(10,10))