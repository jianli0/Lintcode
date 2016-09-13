import sys
class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number
             and the index of the last number
    """
    def subarraySumClosest(self, nums):
        if len(nums) == 0 or nums == None:
            return [0,0]

        old = []
        total = 0
        for i in range(len(nums)) :
            total += nums[i]
            old.append(total)

        new = sorted(old)

        print old
        print new

        minDis = abs(new[0])
        pre = 0
        post = 0
        for i in range(0,len(new) - 1):
            print minDis
            if abs(new[i + 1] - new[i]) < minDis:
                minDis = abs(new[i + 1] - new[i])
                pre = old.index(new[i])
                post = old.index(new[i + 1])

        if minDis == abs(new[0]):
            return [0,0]
        else:
            if pre < post:
                return[pre + 1, post]
            else:
                return[post + 1, pre]



if __name__ == '__main__':
    a = Solution()
    #  print a.subarraySumClosest([-3, 1, 1, -3, 5])
    print a.subarraySumClosest([6, -4, -8, 3 , 1, 7])





