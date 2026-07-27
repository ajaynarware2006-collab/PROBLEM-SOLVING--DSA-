#Move all zeros at the end
def moveZeroes(nums):
    p1=0
    p2=0
    while p2 < len(nums):
        if nums[p2] != 0:
            nums[p1],nums[p2]=nums[p2],nums[p1]
            p1 += 1
        p2 += 1


    return nums

print(moveZeroes([0,1,0,3,12,0,0,2,0,0,0,0]))
print(moveZeroes([0,0,0]))
print(moveZeroes([4,2,4,0,0,3,0,5,1,0]))
print(moveZeroes([1,2]))