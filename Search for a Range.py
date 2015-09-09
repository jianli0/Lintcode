class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : a list of length 2, [index1, index2]
    """
    def searchRange(self, nums, target):
        # write your code here
        if nums == None or len(nums) == 0:
            return [-1, -1]

        return [self.searchforStartorEnd(nums, target, "start"),
                self.searchforStartorEnd(nums, target, "end")]

    def searchforStartorEnd(self, nums, target, direction):
        start,end = 0, len(nums) -1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] == target:
                if direction == "start":
                    end = mid
                elif direction == "end":
                    start = mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid

        if direction == "start":
            if nums[start] == target:
                return start
            if nums[end] == target:
                return end

        if direction == "end":
            if nums[end] == target:
                return end
            if nums[start] == target:
                return start

        return -1



if __name__ == '__main__':
    a = Solution()
    nums1 = []
    nums2 = None
    nums3 = [1, 2, 3, 3, 4, 5, 10]
    nums4 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    print "-"*30
    print a.searchRange(nums1, 3)
    print "-"*30
    print a.searchRange(nums2, 3)
    print "-"*30
    print a.searchRange(nums3, 3)
    print "-"*30
    print a.searchRange(nums4, 5)

