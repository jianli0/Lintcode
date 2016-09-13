import sys
class Solution:
    def maxSubArray(self, nums):
        res = 0
        if not nums:
            return res

        minSum = sys.maxint
        sumResult = 0

        for i in nums:
            sumResult += i
            res = max(res, sumResult - minSum)
            minSum = min(minSum, sumResult)
        return res

a = Solution()
test = [-2, 2, -3, 4, -1, 2, 1, -5, 3]
print a.maxSubArray(test)




