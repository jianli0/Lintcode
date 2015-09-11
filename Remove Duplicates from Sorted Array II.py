class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        # write your code here
        if len(A) < 3:
            return len(A)

        newTail = 1

        for i in range(1, len(A) - 1):
            if A[i - 1] != A[i + 1]:
                A[newTail] = A[i]
                newTail = newTail + 1

        A[newTail] = A[-1]
        return newTail + 1

if __name__ == '__main__':
    a = Solution()
