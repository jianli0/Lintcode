class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        if n <= 1:
            return n

        last = 1
        lastlast = 1

        for i in range(2,n + 1):
            now = last + lastlast
            lastlast = last
            last = now

        return now

a = Solution()
print a.climbStairs(3)

