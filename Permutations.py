# permutation with recursion

class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    def permute(self, S):
        result = []

        if S == None or not len(S):
            return result
        current = []
        S.sort()
        self.Helper(result, current, S)

        return result

    def Helper(self, result, current, S):
        if (len(current) == len(S)):
            result.append(current[:])

        for i in S:
            if i in current:
                continue
            current.append(i)
            self.Helper(result, current, S)
            current.pop()


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

