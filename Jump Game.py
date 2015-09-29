class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        # write your code here
        if not A:
            return False
        can = []

        # init
        for i in range(len(A)):
            can.append(False)

        can[0] = True

        for i in range(1, len(A)):
            for j in range(i):
                if can[j] and (j + A[j] >= i):
                    can[i] = True
                    break
            # debug
            #print can

        return can[-1]

if __name__ == '__main__':
    A = [4,6,9,5,9,3,0]
    a = Solution()
    a.canJump(A)



