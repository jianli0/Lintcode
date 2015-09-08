# permutationII

class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    def __init__(self):
        self.visited = []

    def permuteUnique(self, S):
        result = []

        if S == None or not len(S):
            return result
        current = []

        for i in range(len(S)):
            self.visited.append(0)

        S.sort()
        self.Helper(result, current, self.visited, S)

        return result

    def Helper(self, result, current, visited, S):
        # debug
        # print "jump into Helper function"
        # print "#"*30
        # print visited

        if (len(current) == len(S)):
            result.append(current[:])

        for i in range(len(S)):
            if self.visited[i] == 1 or i != 0 and S[i] == S[i - 1] and self.visited[i - 1] == 0:
                continue
            # debug
            # print "assign value to self.visited"
            # print "i = %d"%i

            self.visited[i] = 1
            current.append(S[i])
            self.Helper(result, current, self.visited, S)
            current.pop()
            self.visited[i] = 0



#test
if __name__ == '__main__':
    S1 = []
    S2 = None
    S3 = [1,2,3]
    S4 = [1,2,2]
    a = Solution()
    # print "-"*20
    # print a.permuteUnique(S1)
    # print "-"*20
    # print a.permuteUnique(S2)
    print "-"*20
    print a.permuteUnique(S3)
    print "-"*20
    print a.permuteUnique(S4)

