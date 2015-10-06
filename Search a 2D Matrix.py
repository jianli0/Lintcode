class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        start, end = 0, len(matrix) - 1

        while start + 1 < end:
            mid = start + (end - start) / 2

            # find it
            # debug
            print "mid is %d" % mid
            print "matrix[mid][0] is %d"% matrix[mid][0]
            if matrix[mid][0] == target:
                return True

            elif matrix[mid][0] < target:
                # do binary search in this row
                if matrix[mid][-1] > target:
                    start1, end1 = 0, len(matrix[mid]) - 1
                    while start1 + 1 < end1:
                        mid1 = start1 + (end1 - start1) / 2
                        # debug
                        print "mid is %d" % mid1
                        print "matrix[mid][mid1] is %d"% matrix[mid][mid1]
                        if matrix[mid][mid1] == target:
                            return True
                        elif matrix[mid][mid1] < target:
                            start1 = mid1
                        else:
                            end1 = mid1
                    return False

                else:
                    start = mid

            elif matrix[mid][0] > target:
                end = mid

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end

        return False




if __name__ == '__main__':
    matrix = [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]]
    target = 3
    a = Solution()

    print a.searchMatrix(matrix, target)
