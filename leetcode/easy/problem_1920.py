class Solution(object):
    def buildArray(self, nums):
        ans=[]
        for i in range(len(nums)):
            if i > (len(nums)-1):
                break
            ans.append(nums[nums[i]])
        
        return ans