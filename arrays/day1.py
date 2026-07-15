# num=[1,2,3]
# print(num*2)


nums=[0,2,1,5,3,4]
ans=[]
for i in range(len(nums)):
    if i > (len(nums)-1):
        break
    print(nums[i])
    print(nums[nums[i]])
    ans.append(nums[nums[i]])
print(ans)