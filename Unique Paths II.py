class Solution:
    """
    @param n and m: positive integer(1 <= n , m <= 100)
    @return an integer
    """

    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        res = []
        # initial
        for i in range(m):
            res.append([])
            for j in range(n):
                res[i].append(None)

        res[0][0] = 1 - obstacleGrid[0][0]

        for i in range(1, m):
            if obstacleGrid[i][0] != 1:
                res[i][0] = res[i - 1][0]
            else:
                res[i][0] = 0

        for j in range(1, n):
            if obstacleGrid[0][j] != 1:
                res[0][j] = res[0][j - 1]
            else:
                res[0][j] = 0


        # for test
        print res

        for i in range(1,m):
            for j in range(1,n):
                # update grid value that is not a obstacle
                if obstacleGrid[i][j] != 1:
                        res[i][j] = res[i - 1][j] + res[i][j - 1]
                else:
                    res[i][j] = 0



        return res[- 1][- 1]




if __name__ == '__main__':
    a = Solution()

    obstacle = [[0,0,0],
                [0,1,0],
                [0,0,0]]

    obstacle1 = [[0,0],[0,0],[0,0],[1,0],[0,0]]
    # print a.uniquePathsWithObstacles(obstacle)
    print a.uniquePathsWithObstacles(obstacle1)

