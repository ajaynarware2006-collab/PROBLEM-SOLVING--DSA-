def runningSum(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = [0] * len(nums)

        prefix[0] = nums[0]

        for i in range(1 , len(nums)):

            prefix[i] = prefix[i-1] + nums[i]
        
        return prefix

print(runningSum(1,2,3,4,5))
print(runningSum(1,1,1,1,1,1))
print(runningSum([3,1,2,10,1]))