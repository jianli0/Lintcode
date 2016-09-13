# time analysis O(n)
# space analysis O(n)

class Solution:
    def largestRectangleArea(self,height):
        if not height:
            return 0
        stk = []
        maxArea = 0
        height.append(-1)

        for i in range(len(height)):
            if len(stk) == 0 or i == 0 or height[i] > height[i - 1]:
                stk.append((height[i] , i))
            else:
                while len(stk) != 0 and stk[-1][0] >= height[i]:
                    (h,index) = stk.pop()
                    print (h,index)
                    print maxArea
                    if len(stk) == 0:
                        width = index + 1
                    else:
                        width = i - stk[-1][1] -1
                    print (width,h)
                    maxArea = max(width * h , maxArea)
                stk.append((height[i], i))
        return maxArea



a = Solution()
test = [5, 4, 1, 2]
test1 = [2, 1, 5, 6, 2, 3]
test2 = [1, 1]
#  print a.largestRectangleArea(test)
print a.largestRectangleArea(test2)
