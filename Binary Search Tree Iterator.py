# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

"""
Example of iterate a tree:
iterator = Solution(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node
"""
class Solution:
    #@param root: The root of binary tree.
    def __init__(self, root):
        # write your code here
        self.q = []
        self.allleftIntoStack(root)


    #@return: True if there has next node, or false
    def hasNext(self):
        # write your code here
        return self.q != []

    #@return: return next node
    def next(self):
        #write your code here
        cur = self.q.pop()
        self.allleftIntoStack(cur.right)
        return cur.val

    def allleftIntoStack(self,root):
        while root:
            self.q.append(root)
            root = root.left


if __name__ == '__main__':

    aa1 = TreeNode(20)
    aa2 = TreeNode(8)
    aa3 = TreeNode(4)
    aa4 = TreeNode(12)
    aa5 = TreeNode(22)

    aa1.left = aa2
    aa1.right = aa5
    aa2.left = aa3
    aa2.right = aa4

    a = Solution(aa1)

    print a.hasNext()
    print a.next()
    print a.next()
    print a.next()
