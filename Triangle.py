class Solution:
    """
    @param triangle: a list of lists of integers.
    @return: An integer, minimum path sum.
    """
    def minimumTotal(self, triangle):
        # write your code here
        if triangle == None or len(triangle) == 0:
            return 0

        n = len(triangle)

        res = []
        for i in range(n):
            res.append([])
            for j in range(n):
                res[i].append(None)

        for i in range(n):
            res[n - 1][i] = triangle[n - 1][i]

        # for test
        # print res

        for i in range(n - 2, -1, -1):
            for j in range(0, i + 1):
                res[i][j] = min(res[i + 1][j], res[i + 1][j + 1]) + triangle[i][j]

        return res[0][0]
        # return res

if __name__ == '__main__':
    a = Solution()
    triangle = [ [2], [3,4], [6,5,7], [4,1,8,3] ]


    print a.minimumTotal(triangle)










