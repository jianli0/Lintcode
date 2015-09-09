class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be inserted
    @return : an integer
    """
    def searchInsert(self, nums, target):
        # write your code here
        if nums == None:
            return
        if len(nums) == 0:
            return 0

        start,end = 0, len(nums) -1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid

        if nums[start] >= target:
            return start
        elif nums[end] >= target:
            return end
        else:
            return end + 1

if __name__ == '__main__':
    a = Solution()
    nums1 = []
    t1 = 5
    nums2 = None
    t2 = 2
    t3 = 7
    t4 = 0
    nums3 = [1, 3, 5, 6]

    print a.searchInsert(nums1, t1)
    print a.searchInsert(nums2, t1)
    print a.searchInsert(nums3, t1)
    print a.searchInsert(nums3, t2)
    print a.searchInsert(nums3, t3)
    print a.searchInsert(nums3, t4)



