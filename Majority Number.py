class Solution:
    """
    @param nums: A list of integers
    @return: The majority number
    """
    def majorityNumber(self, nums):
        # write your code here
        if not nums:
            return

        vote = {}

        for i in nums:
            if i in vote.keys():
                vote[i] += 1
            else:
                vote[i] = 1
            if vote[i] > len(nums) / 2:
                 return i

if __name__ == '__main__':
    a = Solution()
    print a.majorityNumber([0])
