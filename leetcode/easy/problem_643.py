def findMaxAverage(nums, k):
    subnums=float(sum(nums[:k]))
    avgnums=subnums/k
    maxavg=avgnums
    for i in range(k,(len(nums))):
        newsum=subnums + nums[i] - nums[i-k]
        print(newsum,nums[i],nums[i-k])
        newavg=newsum/k
        if maxavg < newavg:
            maxavg = newavg
        subnums=newsum
        
    return maxavg

# print(findMaxAverage([1,12,-5,-6,50,3],4))
print(findMaxAverage([7,4,5,8,8,3,9,8,7,6],7))