def dominantIndex(nums):
        index=0
        largest=nums[0]
        for i in range(1,len(nums)):
            if nums[i] > largest:
                largest=nums[i]
                index=i
        for j in nums:
            if j == nums[index]:
                continue
            if j*2 > nums[index]:
                  return -1
        return index

print(dominantIndex([0,0,3,2]))
print(dominantIndex([3,6,1,0]))