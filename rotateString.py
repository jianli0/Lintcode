class Solution:
    # @param s: a list of char
    # @param offset: an integer
    # @return: nothing
    def rotateString(self, s, offset):
        if not s:
            return
        offset = offset % len(s)

        self.reverse(s, 0, offset)
        self.reverse(s, offset + 1, len(s) - 1)
        self.reverse(s, 0, len(s) - 1)
        print s

    def reverse(self, s, start, end):
        while start < end:
            tmp = s[start]
            s[start] = s[end]
            s[end] = tmp
            start += 1
            end += 1

if __name__ == '__main__':
    a = Solution()
    a.rotateString("abcdefg", 3)
