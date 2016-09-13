import heapq

class Solution:
    def mergeKSortedArrays(self, arrays):
        result = []
        heap = []
        if not arrays:
            return result

        for index, array in enumerate(arrays):
            if array:
                heapq.heappush(heap, (array[0], index, 0))
                # array[0] : value , index : k th array, 0 : place in each array

        while heap:
            val, x, y = heapq.heappop(heap)
            result.append(val)
            if y < (len(arrays[x]) - 1):
                heapq.heappush(heap, (arrays[x][y + 1], x, y + 1))

        return result

test = [
        [1, 3, 5, 7],
        [2, 4, 6],
        [0, 8, 9, 10, 11]
        ]

a = Solution()
print a.mergeKSortedArrays(test)



