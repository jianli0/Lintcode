class Solution:
    """
    @param S: The set of numbers.
    @return: A list of lists. See example.
    """
    def subsets(self, S):
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
            current.append(S[i])
            # debug
            # print "current is now %r" %current
            self.subsetHelper(result, current, S, i + 1)
            current.pop()

#test
if __name__ == '__main__':
    S1 = []
    S2 = None
    S3 = [1,2,3]
    a = Solution()
    print "-"*20
    print a.subsets(S1)
    print "-"*20
    print a.subsets(S2)
    print "-"*20
    print a.subsets(S3)


