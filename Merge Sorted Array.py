class Solution:
    """
    @param A: sorted integer array A which has m elements,
              but size of A is m+n
    @param B: sorted integer array B which has n elements
    @return: void
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        i, j = m - 1, n - 1
        index = m + n - 1

        for i in range(n):
            A [i + m] = B[i]

        if not len(A):
            return B
        if not len(B):
            return A

        while i >= 0 and j >= 0:
            if A[i] > B[j]:
                A[index] = A[i]
                index -= 1
                i -= 1
            else:
                A[index] = B[j]
                index -= 1
                j -= 1

        while i >= 0:
                A[index] = A[i]
                index -= 1
                i -= 1

        while j >= 0:
                A[index] = B[j]
                index -= 1
                j -= 1

if __name__ =='__main__':
    a = Solution()

    A1 = [1, 2, 3]
    B1 = [4, 5]
    print a.mergeSortedArray(A1, 3, B1, 2)
    A2 = [1, 7, 8]
    B2 = [4, 5]
    print a.mergeSortedArray(A2, 3, B2, 2)

