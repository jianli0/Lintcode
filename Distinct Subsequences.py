class Solution:
    # @param S, T: Two string.
    # @return: Count the number of distinct subsequences
    def numDistinct(self, s, t):
        l1, l2 = len(s)+1, len(t)+1

        dp = [[1] * l1 for _ in xrange(l2)]
        self.selfprint(dp)

        for j in xrange(1, l2):
            dp[j][0] = 0
        self.selfprint(dp)

        for i in xrange(1, l2):
            for j in xrange(1, l1):
                print "i = %d, j = %d"%(i,j)
                dp[i][j] = dp[i][j-1] + dp[i-1][j-1]*(s[j-1] == t[i-1])
                self.selfprint(dp)
        return dp[-1][-1]

    def selfprint(self,S):
        for i in S:
            print i
        print




if __name__ == '__main__':
    a = Solution()
    print a.numDistinct("b","b")



