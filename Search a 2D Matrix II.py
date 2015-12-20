class Solution:
    """
    @param matrix: An list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicates the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return 0

        m = len(matrix)
        n = len(matrix[0])

        count = 0
        x = m - 1
        y = 0
        while x >= 0 and y < n:
            if matrix[x][y] > target:
                x -= 1
            elif matrix[x][y] < target:
                y += 1
            else:
                x -= 1
                y += 1
                count += 1
        return count


if __name__ == '__main__':
    a = Solution()
    matrix =\
    [ [1, 3, 5, 7],
      [2, 4, 7, 8],
      [3, 5, 9, 10] ]

    target = 10
    print a.searchMatrix(matrix, target)

