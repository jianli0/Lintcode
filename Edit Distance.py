class Solution:
    # @param word1 & word2: Two string.
    # @return: The minimum number of steps.
    def minDistance(self, word1, word2):
        # write your code here
        dp = []
        for i in range(len(word1) + 1):
            dp.append([])
            for j in range(len(word2) + 1):
                dp[i].append(None)

        for i in range(len(word2) + 1):
            dp[i][0] = i
        for j in range(len(word1) + 1):
            dp[0][j] = j

        for i in range(1, len(word2) + 1):
            for j in range(1, len(word1) + 1):
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + (word1[j - 1] != word2[i - 1]))

        # debug
        # for i in dp:
            # print i

        return dp[-1][-1]







if __name__ == '__main__':
    a = Solution()

    print a.minDistance("word1", "word2")
    print a.minDistance("b", "")
