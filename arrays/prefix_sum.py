arr = [3, 1, 4, 2, 5]

def prefix_sum(arr,L,R):

    prefix = [0] * len(arr)

    prefix[0] = arr[0]

    for i in range(1 , len(arr)):

        prefix[i] = prefix[i-1] + arr[i]

    if L == 0:
        return prefix[R]

    return prefix[R] - prefix[L-1]

print(prefix_sum(arr,1,3))
print(prefix_sum(arr,0,2))
print(prefix_sum(arr,1,4))
print(prefix_sum(arr,2,4))
print(prefix_sum(arr,3,3))

arr = [5, -2, 4, -3, 7]

print(prefix_sum(arr,1,3))
print(prefix_sum(arr,0,2))
print(prefix_sum(arr,1,4))
print(prefix_sum(arr,2,4))
print(prefix_sum(arr,3,3))