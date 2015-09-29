class Solution:
    """
    @param grid: a list of lists of integers.
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        # write your code here
        if not len(grid) or not len(grid[0]):
            return 0

        m = len(grid)
        n = len(grid[0])

        # init
        res = []
        for i in range(m):
            res.append([])
            for j in range(n):
                res[i].append(None)

        res[0][0] = grid[0][0]

        # debug
        # print res

        for i in range(1, n):
            res[0][i] = res[0][i - 1] + grid[0][i]
        for i in range(1, m):
            print i,
            res[i][0] = res[i - 1][0] + grid[i][0]

        for i in range(1, m):
            for j in range(1, n):
                res[i][j] = min(res[i - 1][j], res[i][j - 1]) + grid[i][j]

        # print res
        return res[- 1][- 1]

if __name__ == '__main__':
    grid = [[1, 2, 3, 4],
            [2, 8, 7, 9],
            [9, 7, 6, 3],
            [2, 2, 1, 7]
            ]
    grid1 = [[1,4,8,6,2,2,1,7],[4,7,3,1,4,5,5,1],[8,8,2,1,1,8,0,1],[8,9,2,9,8,0,8,9],[5,7,5,7,1,8,5,5],[7,0,9,4,5,6,5,6],[4,9,9,7,9,1,9,0]]
    a = Solution()
    print a.minPathSum(grid1)
