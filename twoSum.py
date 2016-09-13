class Solution:
    """
    @param numbers : An array of Integer
    @param target : target = numbers[index1] + numbers[index2]
    @return : [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        if numbers == None or len(numbers) == 0:
            return None

        new = sorted(numbers)
        p1 = 0
        p2  = len(numbers) - 1

        while p1 < p2:
            print "p1 : %d p2: %d"%(p1,p2)
            if (new[p1] + new[p2]) == target:
                break;
            elif (new[p1] + new[p2]) > target:
                p2 -= 1
            else:
                p1 += 1

        if p1 >= p2:
            return None
        else:
            index1 = numbers.index(new[p1])
            index2 = numbers.index(new[p2])
            print index1,index2
            if index1 == index2:
                index2 = numbers.reverse().index(new[p2])

            if index1 < index2:
                return [index1 + 1, index2 + 1]
            else :
                return [index2 + 1, index1 + 1]


if __name__ == '__main__':
    a = Solution()
    print a.twoSum([2, 7, 11, 15] , 9)
