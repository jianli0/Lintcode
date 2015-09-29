class Solution:
    # @param s: A string s
    # @param dict: A dictionary of words dict
    def wordBreak(self, s, dict):
        # write your code here
        dp = [False] * (1 + len(s))
        dp[0] = True

        for i in range(1,len(dp)):
            for j in range(i):
                if s[j : i] in dict and dp[j]:
                    # debug
                    # print "j : %d  i:%d"%(j,i)
                    # print s[j : i + 1]
                    dp[i] = True
            # print dp

        return dp[-1]

if __name__ == '__main__':
    a = Solution()
    s = "leetcode"
    dict1 = ["leet", "code"]
    print a.wordBreak(s, dict1)

