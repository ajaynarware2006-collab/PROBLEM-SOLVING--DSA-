numbers=[1,2,4,5,3]
runningsum=[]
sum=0
for i in numbers:
    sum+=i
    runningsum.append(sum)

print(runningsum)