def sortedSquares(nums):
    n=len(nums)
    newnums=[None]*n
    p1=0
    p2=n-1
    for i in range(p2,-1,-1):
        if abs(nums[p1]) < abs(nums[p2]):
            newnums[i]=nums[p2]**2
            p2 -= 1
        else:
            newnums[i]=nums[p1]**2
            p1 += 1
            
    return newnums

print(sortedSquares([-4,-1,0,3,10]))
print(sortedSquares([-7,-3,2,3,11]))
print(sortedSquares([-7,-3,-2,-3,-11]))
print(sortedSquares([-5,-3,-2,-1]))
