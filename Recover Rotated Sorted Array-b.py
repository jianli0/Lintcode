class Solution:
    """
    @param nums: The rotated sorted array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        if nums == None or len(nums) == 0:
            return

        for i in range(len(nums) - 1):
            if (nums[i] > nums[i + 1]):
                # debug
                # print "%d %d" % (nums[i], nums[i + 1])
                # print "i is %d" %i
                self.reverse(nums, 0, i)
                self.reverse(nums, i + 1, len(nums) - 1)
                self.reverse(nums, 0, len(nums) - 1)

                # for test
                # return nums

    def reverse(self, nums, start, end):
        i = start
        j = end
        while i < j:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i += 1
            j -= 1

if __name__ == '__main__':
    a = Solution()
    nums1 = []
    nums2 = None
    nums3 = [4, 5, 1, 2, 3]
    nums4 = [1, 2, 3, 4, 5]

    print a.recoverRotatedSortedArray(nums1)
    print a.recoverRotatedSortedArray(nums2)
    print a.recoverRotatedSortedArray(nums3)
    print a.recoverRotatedSortedArray(nums4)
