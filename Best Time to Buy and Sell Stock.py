class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        if not prices:
            return 0
        dp = []
        dp.append(0)
        minPrice = prices[0]
        for i in range(1,len(prices)):
            dp.append(max(dp[i - 1], prices[i] - minPrice))
            if prices[i] < minPrice:
                minPrice = prices[i]
        return dp[-1]


if __name__ == '__main__':
    a = Solution()
    print a.maxProfit([3,2,3,1,2])

