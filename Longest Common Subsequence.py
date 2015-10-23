class Solution:
    # @param A, B: Two string.
    # @return: the length of the longest common substring.
    def longestCommonSubstring(self, A, B):
        # write your code here
        l1, l2 = len(A), len(B)

        dp = [[0]*l1 for _ in range(l2)]

        maxlen = 0
        for i in range(l2):
            for j in range(l1):
                length = 0
                while(j + length < l1 and i + length < l2 and
                        A[j + length] == B[i + length]):
                    length += 1
                    if length > maxlen:
                        maxlen = length
        return maxlen

if __name__ == '__main__':
    a = Solution()
    A = "ABCD"
    B = "CBCE"
    print a.longestCommonSubstring(A,B)

