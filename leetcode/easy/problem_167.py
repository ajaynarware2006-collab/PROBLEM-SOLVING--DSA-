def twoSum(numbers, target):
    p1=0
    p2=len(numbers)-1
    while p1 < p2:
        currentsum= numbers[p1] + numbers[p2]
        if currentsum==target:
            return [p1+1,p2+1]
        if currentsum > target:
            p2 -= 1
        elif currentsum < target:
            p1 += 1



print(twoSum([2,7,11,15],18))
