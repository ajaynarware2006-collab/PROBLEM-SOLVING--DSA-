class Solution(object):
    def findMaxLength(self, nums):
        prefix_sum = 0
        max_len = 0

        first = {0: -1}

        for i, num in enumerate(nums):

            if num == 0:
                prefix_sum -= 1
            else:
                prefix_sum += 1

            if prefix_sum in first:
                length = i - first[prefix_sum]
                max_len = max(max_len, length)
            else:
                first[prefix_sum] = i

        return max_len

