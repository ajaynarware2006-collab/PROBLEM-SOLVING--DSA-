class Solution(object):
    def pivotIndex(self, nums):
        n = len(nums)

        newnums = [0] * n
        newnums[0] = nums[0]

        for i in range(1, n):
            newnums[i] = newnums[i - 1] + nums[i]

        total = newnums[n - 1]

        for i in range(n):

            if i == 0:
                left_sum = 0
            else:
                left_sum = newnums[i - 1]

            right_sum = total - newnums[i]

            if left_sum == right_sum:
                return i

        return -1