class Solution:
    def intersection(self, nums1, nums2):
        rst = []
        if not (nums1 and nums2) :
            return rst
        n1 = {}
        for i in nums1:
            n1[i] = 1

        for j in nums2:
            if j in n1:
                rst.append(j)

        return list(set(rst))

a = Solution()
test1 = [1,2,2,1]
test2 = [2,2]
print a.intersection(test1, test2)
