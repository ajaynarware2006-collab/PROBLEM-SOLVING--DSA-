nums=[1,1,1,1,0,1,1,0,1]
count=0
MaxConsecutiveOnes=0
lenth=len(nums)
for i in range(lenth):
    binary=nums[lenth-1]
    if binary == 1:
        count+=1
        if count > MaxConsecutiveOnes:
            MaxConsecutiveOnes = count
    else:
        count=0
    lenth-=1

print(MaxConsecutiveOnes)