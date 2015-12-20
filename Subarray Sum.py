class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number
             and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        dic = {}
        ans = []

        res = 0
        dic[0] = -1

        for i in range(len(nums)):
            res += nums[i]
            if res in dic.keys():
                ans.append(dic[res] + 1)
                ans.append(i)
                return ans
            dic[res] = i

        return ans


if __name__ == '__main__':
    a = Solution()
    nums = [-3, 1, 2, -3, 4]
    print a.subarraySum(nums)

