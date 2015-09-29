class Solution:
    """
    @param nums: The integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        f = []
        if not nums:
            return 0

        for i in range(len(nums)):
            f.append(1)

        for i in range(1,len(f)):
            for j in range(i):
                if nums[i] >= nums[j] and f[j] + 1 > f[i]:
                    f[i] = f[j] + 1

        return max(f)

if __name__ == '__main__':
    a = Solution()
    b = [4,2,4,5,3,7]
    print a.longestIncreasingSubsequence(b)
