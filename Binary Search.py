class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0
    def binarySearch(self, nums, target):
        # write your code here
        if nums == None or len(nums) == 0:
            return -1

        start,end = 0, len(nums) -1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] == target:
                end = mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end

        return -1


if __name__ == '__main__':
    a = Solution()
    nums1 = []
    nums2 = None
    nums3 = [1, 2, 3, 3, 4, 5, 10]

    print "-"*30
    print a.binarySearch(nums1, 3)
    print "-"*30
    print a.binarySearch(nums2, 3)
    print "-"*30
    print a.binarySearch(nums3, 3)

