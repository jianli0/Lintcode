class Solution:
    """
    @param A: An integer array.
    @param B: An integer array.
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        # write your code here
        A = A + B
        A.sort()

        return (self.findMedian(A))

    def findMedian(self, L):

        if len(L) == 0:
            return
        else:
            if len(L) % 2 == 1:
                return (L[len(L) / 2] / 1.0)
            else:
                return ((L[len(L) / 2] + L[len(L) / 2 - 1]) / 2.0)


if __name__ == '__main__':
    a = Solution()

    # return 3.5
    A1 = [1, 2, 3, 4, 5, 6]
    B1 = [2, 3, 4, 5]

    # return 3
    A2 = [1, 2, 3]
    B2 = [4, 5]

    # return 2
    A3 = [1, 2, 3]
    B3 = []

    # return 2
    A4 = []
    B4 = []

    print "-"*20
    print a.findMedianSortedArrays(A1, B1)
    print "-"*20
    print a.findMedianSortedArrays(A2, B2)
    print "-"*20
    print a.findMedianSortedArrays(A3, B3)
    print "-"*20
    print a.findMedianSortedArrays(A4, B4)
