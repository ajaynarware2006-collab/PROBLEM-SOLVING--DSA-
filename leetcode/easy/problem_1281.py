def subtractProductAndSum(n):
    product=1
    sum=0
    while n > 0:
        value= n % 10
        product *= value
        sum += value

        n = n//10
    return (product - sum)