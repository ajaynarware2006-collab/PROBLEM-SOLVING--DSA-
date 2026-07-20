nums=[2,32,23,43,27,56,-1,-34,-24,78,54,-40]

#practice 1
sum=0
for i in nums:
    sum+=i
print(sum)


#practice 2
count=0
for i in nums:
    if i > 50:
        count += 1

print(count)


#practice 3
negative=0
for i in nums:
    if i < 0:
        negative += 1
print(negative)