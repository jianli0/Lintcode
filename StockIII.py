import sys

class Solution:
    def maxProfit(self, prices):
        maxP = 0
        if not prices:
            return maxP

        minLeft = sys.maxint
        maxLeftResult = 0
        maxLeftResults = []

        maxRight = -sys.maxint
        maxRightResult = 0
        maxRightResults = []

        for i in range(len(prices)):
            maxLeftResult = max(maxLeftResult, prices[i] - minLeft)
            minLeft = min(minLeft, prices[i])
            maxLeftResults.append(maxLeftResult)

        for i in range(len(prices) - 1, -1, -1):
            maxRightResult = max(maxRightResult, maxRight - prices[i])
            maxRight = max(maxRight, prices[i])
            maxRightResults.append(maxRightResult)

        maxRightResults.reverse()

        for i in range(len(prices)):
            maxP = max(maxP, maxLeftResults[i] + maxRightResults[i])
        return maxP


a = Solution()
test = [4, 4, 6, 1, 1, 4, 2, 5]
print a.maxProfit(test)






