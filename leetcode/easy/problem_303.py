class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.Numarray = [0] * len(self.nums)

        self.Numarray[0] = self.nums[0]

        for i in range(1 , len(self.nums)):

            self.Numarray[i] = self.Numarray[i-1] + self.nums[i]

        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """

        if left == 0:
            return self.Numarray[right]
        
        return self.Numarray[right] - self.Numarray[left-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)