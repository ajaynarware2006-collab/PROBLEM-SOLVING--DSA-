def removeElement(nums, val):
    if nums == []:
        return 0
    n = len(nums)
    p2 = n-1
    count=0
    for p1 in range(n):
        # print()
        # print(p1,p2)
        # print(nums)
        if nums[p2] == val:
            # print("yes1")
            p2 -= 1
            count+=1
        elif nums[p1] != val:
            p1 += 1

        else:
            # print("yes 2")
            nums[p1] , nums[p2] = nums[p2] , nums[p1]
            count+=1
            p2 -= 1
        if p1 >= p2:
            break
        # print(nums)
        
        # print(nums)
    # print(nums)
    # print(count)
    print(nums)
    return n - count

# print(removeElement([3,2,2,3],3))
# print(removeElement([0,1,2,2,3,0,4,2],2))
# print(removeElement([1,2,2,2,2,2],2))
# print(removeElement([],2))
# print(removeElement([1],2))
# print(removeElement([1,3,4,5,6],2))
# print(removeElement([2,2,3],2))
print(removeElement([3,1,3,3,3],3))
