# remove the duplicates and do subset

class Solution:
    """
    @param S: The set of numbers.
    @return: A list of lists. See example.
    """
    def subsetsWithDup(self, S):
        result = []

        if S == None or not len(S):
            # debug
            # print "about to return"
            return result
        current = []
        S.sort()
        self.subsetHelper(result, current, S, 0)

        return result

    def subsetHelper(self, result, current, S, pos):
        result.append(current[:])
        # debug
        # print "result is now %r" %result

        for i in range(pos,len(S)):
            if (i != pos and S[i] == S[i - 1]):
                # debug
                # print "pos is %d" %i
                continue

            current.append(S[i])
            # debug
            # print "current is now %r" %current
            self.subsetHelper(result, current, S, i + 1)
            current.pop()

#test
if __name__ == '__main__':
    # S1 = []
    # S2 = None
    # S3 = [1,2,3]
    S4 = [1, 2, 2]
    S5 = [0]
    S6 = [1, 1]

    a = Solution()
    # print "-"*20
    # print a.subsetsWithDup(S1)
    # print "-"*20
    # print a.subsetsWithDup(S2)
    # print "-"*20
    # print a.subsetsWithDup(S3)
    print "-"*20
    print a.subsetsWithDup(S4)
    print "-"*20
    print a.subsetsWithDup(S5)
    print "-"*20
    print a.subsetsWithDup(S6)


