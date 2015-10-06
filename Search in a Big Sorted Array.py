class Solution:
    # @param {int[]} A an integer array
    # @param {int} target an integer
    # @return {int} an integer
    def searchBigSortedArray(self, A, target):
        # write your code here
        if not A:
            return -1

        start , end = 0, len(A) -1
        while start + 1 < end:
            mid = start +(end - start) / 2
            if A[mid] == target:
                end = mid
            elif A[mid] > target:
                end = mid
            else:
                start = mid

        if A[start] == target:
            return start
        elif A[end] == target:
            return end
        return -1







if __name__ == '__main__':
    b = [1, 3, 6, 9, 21]
    target1 = 3
    target2 = 4
    a = Solution()

    print a.searchBigSortedArray(b, target1)
    print a.searchBigSortedArray(b, target2)
