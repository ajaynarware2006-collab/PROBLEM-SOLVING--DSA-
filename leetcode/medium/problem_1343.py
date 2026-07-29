def numOfSubarrays(arr, k, threshold):
    if arr == []:
        return 0
    subsum=sum(arr[:k])
    avg=subsum/k
    count=0
    if avg >= threshold:
        count += 1
    for i in range(k,len(arr)):
        subsum=subsum - arr[i-k] + arr[i]
        avg = subsum/k
        if avg >= threshold:
                count += 1

    return count

print(numOfSubarrays([2,2,2,2,5,5,5,8],3,4))
print(numOfSubarrays([1,1,1,1,1],2,1))
print(numOfSubarrays([1,2,3,4,5],2,4))
print(numOfSubarrays([5,5,5,5],4,5))
print(numOfSubarrays([7],1,7))
print(numOfSubarrays([1,2,3,4],4,3))
print(numOfSubarrays([0,0,0,0],2,0))
        
    