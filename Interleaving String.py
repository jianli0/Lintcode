class Solution:
    """
    @params s1, s2, s3: Three strings as description.
    @return: return True if s3 is formed by the interleaving of
             s1 and s2 or False if not.
    @hint: you can use [[True] * m for i in range (n)] to allocate a n*m matrix.
    """
    def isInterleave(self, s1, s2, s3):
        # write your code here
        len1 = len(s1) + 1
        len2 = len(s2) + 1
        len3 = len(s3)

        dp = [[True] * len2 for i in range(len1)]
        if len1 + len2 - 2 != len3:
            return False
        #  print " len1 2 3"
        #  print len1,len2,len3
        for i in range(1,len1):
            dp[i][0] = dp[i - 1][0] and (s1[i - 1] == s3[i - 1])

        for j in range(1,len2):
            dp[0][j] = dp[0][j - 1] and (s2[j - 1] == s3[i - 1])

        for i in range(1, len1):
            for j in range(1, len2):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or\
                (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
            #  for i in dp:
                #  print i
            #  print "-"*30
        return dp[-1][-1]

if __name__ == '__main__':
    a = Solution()
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    s31 = "aadbbbaccc"
    #  print a.isInterleave(s1, s2, s3)
    #  print a.isInterleave(s1, s2, s31)

    s11 = "a"
    s12 = ""
    s13 = "a"
    print a.isInterleave(s11, s12, s13)
