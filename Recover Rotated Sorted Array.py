#debug
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
                print "%d %d" % (nums[i], nums[i + 1])
                print "i is %d" %i
                pre = nums[0 : i + 1]
                post = nums[i + 1 : len(nums)]

                pre.reverse()
                post.reverse()
                nums = pre + post

                nums.reverse()
                # return nums

        # for test
        # return nums



if __name__ == '__main__':
    a = Solution()
    nums1 = []
    nums2 = None
    nums3 = [4, 5, 1, 2, 3]
    nums4 = [1, 2, 3, 4, 5]
    nums5 = [5, 4, 3, 2, 1]

    print a.recoverRotatedSortedArray(nums1)
    print a.recoverRotatedSortedArray(nums2)
    print a.recoverRotatedSortedArray(nums3)
    print a.recoverRotatedSortedArray(nums4)
    print a.recoverRotatedSortedArray(nums5)
