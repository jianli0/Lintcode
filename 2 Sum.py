class Solution:
    """
    @param numbers : An array of Integer
    @param target : target = numbers[index1] + numbers[index2]
    @return : [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        if not numbers:
            return None

        for i in range(len(numbers)):
            if (target - numbers[i]) in numbers[i+1 : ]:
                return [i + 1, numbers.index(target - numbers[i]) + 1]

        return None

if __name__ == '__main__':
    a = Solution()
    numbers = [2, 7, 11, 15]
    target = 9
    print a.twoSum(numbers, target)



