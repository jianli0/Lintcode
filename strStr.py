class Solution:
    def strStr(self, source, target):
        if target == "":
            return 0
        else:
            if not source:
                return -1
            elif not target:
                for i in range(len(source)):
                    if source[i] == target[0]:
                        if source[i:i + len(target)] == target:
                            return i
                # write your code here
        return -1


#test
print Solution().strStr("source","target")
print Solution().strStr("abcdabcdefg", "bcd")
print Solution().strStr("", "")
print Solution().strStr(None, "a")
print Solution().strStr("abc", None)
