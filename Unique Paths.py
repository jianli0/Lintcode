class Solution:
    """
    @param n and m: positive integer(1 <= n , m <= 100)
    @return an integer
    """
    def uniquePaths(self, m, n):
        if m == 0 or n == 0:
            return 0

        res = []
        # initial
        for i in range(m):
            res.append([])
            for j in range(n):
                res[i].append(None)

        for i in range(m):
            res[i][0] = 1

        for j in range(n):
            res[0][j] = 1


        for i in range(1,m):
            for j in range(1,n):
                res[i][j] = res[i - 1][j] + res[i][j - 1]

        return res[m - 1][n - 1]



if __name__ == '__main__':
    a = Solution()
    print a.uniquePaths(3,7)
