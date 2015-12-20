class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    return: The maximum length of the small pieces.
    """
    def woodCut(self, L, k):
        # write your code here
        if sum(L) < k:
            return 0
        start, end = 1, max(L)

        while start + 1 < end:
            mid = (start + end) / 2
            pieces = sum([(i / mid) for i in L])
            if pieces >= k:
                start = mid
            else:
                end = mid

        if sum([(i / end) for i in L]) >= k:
            return end
        return start


if __name__ == '__main__':
    a = Solution()
    L = [232, 124, 456]
    k = 7
    print a.woodCut(L, k)

