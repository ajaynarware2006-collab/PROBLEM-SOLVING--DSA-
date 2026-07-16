# numbers = [12, 45, 7, 19, 33, 28]

# print("task 2 and 3")
# for i in range(len(numbers)):
#     print(f"Index {i} -> {numbers[i]}")

# print("task 4")
# count=0
# for i in numbers:
#     if i > 20:
#         count+=1
    
# print(f"Total numbers greater than 20 = {count}")

# max=0
# for i in numbers:
#     if max < i:
#         max=i
    
# print(f"Max number is {max}")

# #practice

# runningsum=[]
# sum=0
# for i in numbers:
#     sum+=i
#     runningsum.append(sum)

# print(runningsum)


#1672
# accounts=[[2,8,7],[7,1,3],[1,9,5]]
# max=0
# for i in accounts:
#     sum=0
#     for j in i:
#         sum+=j
#         if sum > max:
#             max=sum
    
# print(max)
        

nums=[1,1,1,1,0,1,1,0,1]
count=0
MaxConsecutiveOnes=0
lenth=len(nums)
for i in range(lenth):
    binary=nums[lenth-1]
    if binary == 1:
        count+=1
        if count > MaxConsecutiveOnes:
            MaxConsecutiveOnes = count
    else:
        count=0
    lenth-=1

print(MaxConsecutiveOnes)