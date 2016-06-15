class Solution:
    """
    @param triangle: a list of lists of integers.
    @return: An integer, minimum path sum.
    """
    # up down
    def minimumTotal(self,triangle):
        if not triangle:
            return 0
        res = [[0]*len(triangle[i]) for i in range(len(triangle))]

        #  initial
        res[0][0] = triangle[0][0]

        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j - 1 < 0:
                    res[i][j] = triangle[i][j] + res[i - 1][j]
                elif j == len(triangle[i]) - 1:
                    res[i][j] = triangle[i][j] + res[i - 1][j - 1]
                else:
                    res[i][j] = triangle[i][j] + min(res[i - 1][j - 1], res[i - 1][j])

        return min(res[len(triangle) - 1])



    # down up
    #  def minimumTotal(self, triangle):
        #  if not triangle:
            #  return 0

        #  res = [[] for i in range(len(triangle))]

        #  #initial
        #  for i in triangle[-1]:
            #  res[-1].append(i)

        #  for i in range(len(triangle) - 2, -1,-1):
            #  #  print triangle[i]
            #  for j in range(len(triangle[i])):
                #  #  print triangle[i][j] , res[i + 1][j] , res[i + 1][j + 1]
                #  res[i].append(triangle[i][j]+ min(res[i + 1][j], res[i + 1][j + 1]))
            #  #  print res

        #  return res[0][0]


a = Solution()
triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
print a.minimumTotal(triangle)

