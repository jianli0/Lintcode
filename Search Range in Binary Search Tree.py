"""
Definition of TreeNode:
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: The root of the binary search tree.
    @param k1 and k2: range k1 to k2.
    @return: Return all keys that k1<=key<=k2 in ascending order.
    """
    def searchRange(self, root, k1, k2):
        a = self.searchRangeHelper(root, k1, k2, [])
        a.sort()
        return a



    def searchRangeHelper(self, root, k1, k2, result):

        # Debug
        print "result is now %r" %result

        if root == None:
            print "return before"
            return result

        if root.val < k1:
            self.searchRangeHelper(root.right, k1, k2, result)
        elif root.val > k2:
            self.searchRangeHelper(root.left, k1, k2, result)
        else:
            result.append(root.val)
            self.searchRangeHelper(root.left, k1, k2, result)
            self.searchRangeHelper(root.right, k1, k2, result)

        # Debug
        print "return later"

        return result

if __name__ == '__main__':
    a = Solution()

    aa1 = TreeNode(20)
    aa2 = TreeNode(8)
    aa3 = TreeNode(4)
    aa4 = TreeNode(12)
    aa5 = TreeNode(22)

    aa1.left = aa2
    aa1.right = aa5
    aa2.left = aa3
    aa2.right = aa4

    print a.searchRange(aa1, 10, 22)
    print a.searchRange(None, None, None)
    print a.searchRange(aa1, 1, 3)
    print a.searchRange(aa1, 21, 22)
