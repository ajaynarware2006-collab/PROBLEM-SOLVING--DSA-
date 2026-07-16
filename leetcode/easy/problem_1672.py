accounts=[[2,8,7],[7,1,3],[1,9,5]]
max=0
for i in accounts:
    sum=0
    for j in i:
        sum+=j
        if sum > max:
            max=sum
    
print(max)