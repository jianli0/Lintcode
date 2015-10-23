class Solution:
    # @param A, B: Two string.
    # @return: the length of the longest common substring.
    def longestCommonSubstring(self, A, B):
        # write your code here
        l1, l2 = len(A) + 1, len(B) + 1

        dp = [[0]*l1 for _ in range(l2)]
        # debug
        # self.selfprint(dp)
        for i in range(1,l2):
            for j in range(1,l1):
                if A[j-1] != B[i-1]:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                else:
                    dp[i][j] = dp[i-1][j-1] + 1


                # debug
                # self.selfprint(dp)

        return dp[-1][-1]

    # def selfprint(self,S):
        # for i in S:
            # print i
        # print

if __name__ == '__main__':
    a = Solution()
    A = "ABCD"
    B = "CBCE"
    print a.longestCommonSubstring(A,B)

