class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        # write your code here
        dp = []
        for i in range(len(s) + 1):
            dp.append(i)

        for i in range(1,len(dp)):
            for j in range(i):
                if self.isPa(s[j:i]):
                    if dp[i] > dp[j] + 1:
                        dp[i] = dp[j] + 1
        # debug
        # print dp
        return dp[-1] - 1

    def isPa(self, s):
        return s == s[::-1]

if __name__ == '__main__':
    a = Solution()
    s = "abbacdca"
    print a.minCut(s)


