class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        if not nums:
            return 0

        globalMax = nums[0]
        localMax = nums[0]

        for i in range(1, len(nums)):
            localMax = max(nums[i], localMax + nums[i])
            globalMax = max(localMax, globalMax)

        return globalMax


if __name__ == '__main__':
    a = Solution()
    nums = [-2, 2, -3, 4, -1, 2, 1, -5, 3]
    print a.maxSubArray(nums)
