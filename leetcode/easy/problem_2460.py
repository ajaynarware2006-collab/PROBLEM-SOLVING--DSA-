def applyOperations(nums):
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        p1 = 0
        for p2 in range(n):
            if nums[p2] != 0:
                nums[p1] = nums[p2]
                p1 += 1

        while p1 < n:
            nums[p1] = 0
            p1 += 1

        return nums

print(applyOperations([1,2,2,1,1,0]))
print(applyOperations([]))
print(applyOperations([1,1,1,1,1,1,1]))
print(applyOperations([[0,1]]))