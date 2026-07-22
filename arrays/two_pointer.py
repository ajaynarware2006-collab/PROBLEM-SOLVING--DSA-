arr=[1,3,5,7,9]

p1=0
p2=len(arr)-1

while p1 < p2:
    if arr[p1]+arr[p2] == 10:
        print(p1 , p2)
    p1 += 1
    p2 -= 1

def rev(arr):
    p1=0
    p2=len(arr)-1
    while p1 < p2:
        arr[p1],arr[p2]=arr[p2],arr[p1]
    
    return arr

print(rev([1,3,5,7,9]))
