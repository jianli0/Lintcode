class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : an integer
    """
    def search(self, A, target):
        # write your code here
        if A == None or len(A) == 0:
            return -1

        start, end = 0, len(A) - 1

        while start + 1 < end:
            mid = (start + end) / 2
            if (A[mid] == target):
                return mid
            if (A[start] < A[mid]):
                if(A[start] <= target and target <= A[mid]):
                    end = mid
                else:
                    start = mid
            else:
                if(A[mid] <= target and target <= A[end]):
                    start = mid
                else:
                    end = mid

        if A[start] == target:
            return start
        elif A[end] == target:
            return end

        return -1

if __name__ == '__main__':
    a = Solution()
    nums1 = []
    nums2 = None
    nums3 = [4, 5, 1, 2, 3]

    print "-"*30
    print a.search(nums1, 3)
    print "-"*30
    print a.search(nums2, 3)
    print "-"*30
    print a.search(nums3, 1)
    print "-"*30
    print a.search(nums3, 0)

