#414
# def thirdMax(nums):
#         nums=set(nums)
#         if len(nums) < 3:
#              return max(nums)
        
#         first = float("-inf")
#         second = float("-inf")
#         third = float("-inf")
        
#         for i in nums:

#             if i > first:
#                 third = second
#                 second = first
#                 first = i

#             elif i > second:
#                 third = second
#                 second = i
            
#             elif i > third:
#                 third=i

#         return third
        
# print(thirdMax([2,2,3,1]))
# print(thirdMax([1,1,2]))

# #1464
# def maxProduct(self, nums):
