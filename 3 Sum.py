class Solution:
    """
    @param numbersbers : Give an array numbersbers of n integer
    @return : Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        result = []
        if not numbers:
            return result
        numbers.sort()

        for i in range(0, len(numbers) - 2):
            if (i != 0 and numbers[i] == numbers[i - 1]):
                continue;
            left = i + 1
            right = len(numbers) - 1
            while left < right:
                if (numbers[left] + numbers[right]) > -numbers[i]:
                    right -= 1
                elif (numbers[left] + numbers[right]) < -numbers[i]:
                    left += 1
                else:
                    result.append([numbers[i], numbers[left] , numbers[right]])
                    right -= 1
                    left += 1
                    while(left < right and numbers[left] == numbers[left - 1]):
                        left += 1;
                    while(left < right and numbers[right] == numbers[right + 1]):
                        right -= 1;

        return result


a = Solution()
test = [-1, 0, 1, 2, -1, -4]
print a.threeSum(test)
