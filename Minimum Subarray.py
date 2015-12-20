class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """
    def minSubArray(self, nums):
        # write your code here
        if not nums:
            return 0

        globalMin = nums[0]
        localMin = nums[0]

        for i in range(1, len(nums)):
            localMin = min(nums[i], localMin + nums[i])
            globalMin = min(localMin, globalMin)

        return globalMin


if __name__ == '__main__':
    a = Solution()
    nums = [-2, 2, -3, 4, -1, 2, 1, -5, 3]
    print a.minSubArray(nums)
