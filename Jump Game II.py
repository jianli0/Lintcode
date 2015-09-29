class Solution:
    # @param A, a list of integers
    # @return a boolean
    def jump(self, A):
        # write your code here
        if not A:
            return None

        step = []

        # init
        for i in range(len(A)):
            step.append(None)

        step[0] = 0

        for i in range(1, len(A)):
            for j in range(i):
                if step[j] != None and j + A[j] >= i:
                    step[i] = step[j] + 1
                    break

        return step[-1]

if __name__ == '__main__':
    A = [4,6,9,5,9,3,0]
    a = Solution()
    print a.jump(A)



