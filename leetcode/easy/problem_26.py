# remove duplicates from the array and return number of unique numbers
def removeDuplicates(nums):
    p1=0
    p2=1
    for i in range(1,len(nums)):
        if nums[p1] == nums[p2]:
            p2 += 1
        elif nums[p1] != nums[p2]:
            p1 +=1
            nums[p1],nums[p2]=nums[p2],nums[p1]
            p2 += 1
        
    return p1+1

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
