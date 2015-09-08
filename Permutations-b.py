class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        if nums == None or not len(nums):
            return []

        nums.sort()


#test
if __name__ == '__main__':
    S1 = []
    S2 = None
    S3 = [1,2,3]
    a = Solution()
    print "-"*20
    print a.permute(S1)
    print "-"*20
    print a.permute(S2)
    print "-"*20
    print a.permute(S3)

