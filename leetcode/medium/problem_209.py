def minSubArrayLen(target, nums):
    left = 0
    current_sum = 0
    minimum = float("inf")

    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum >= target:
            minimum = min(minimum, right - left + 1)
            current_sum -= nums[left]
            left += 1
    if minimum == float("inf"):
        return 0
    return minimum

print(minSubArrayLen(7,[2,3,1,2,4,3]))
print(minSubArrayLen(5,[5]))
print(minSubArrayLen(5,[6]))
print(minSubArrayLen(5,[3]))
print(minSubArrayLen(15,[1,2,3,4,5]))
print(minSubArrayLen(150,[1,2,3,4,5]))
print(minSubArrayLen(8,[1,2,3,4,9]))
print(minSubArrayLen(8,[9,1,2,3,4]))
print(minSubArrayLen(11,[1,2,6,5,1]))
print(minSubArrayLen(5,[2,3,2,3]))
print(minSubArrayLen(8,[1,4,4]))
print(minSubArrayLen(6,[3,3,1,1])) 
print(minSubArrayLen(4,[1,1,1,1,1])) 
print(minSubArrayLen(9,[3,3,3,3])) 
print(minSubArrayLen(100000,[99999,1])) 
print(minSubArrayLen(15,[5,1,3,5,10,7,4,9,2,8])) 
