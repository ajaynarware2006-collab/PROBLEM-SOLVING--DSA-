nums=[8,1,2,2,3]
index=0
new=[]
for i in range(len(nums)):
    sum=0
    for j in range(len(nums)):
        if index != j:
            if nums[index] > nums[j]:
                sum+=1
    new.append(sum)
    index+=1

print(new)