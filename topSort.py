from sets import Set

# Definition for a Directed graph node
class DirectedGraphNode:
   def __init__(self, x):
       self.label = x
       self.neighbors = []

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class Solution:
    def topSort(self, graph):
        res = []
        if not graph:
            return res

        allNodes = Set(graph)
        nbs = Set([])

        for n in graph:
            for nb in n.neighbors:
                nbs.add(nb)

        start = allNodes - nbs
        if len(start) == 1:
            startNode = list(start)[0]

        # find start node and do bfs
        q = Queue()
        visited = Set([])

        q.enqueue(startNode)
        while not q.isEmpty():
            node = q.dequeue()
            visited.add(node)
            for i in node.neighbors:
                if i in visited:
                    continue
                else:
                    q.enqueue(i)

        res = list(visited)

        return res

a = Solution()

a0 = DirectedGraphNode(0)
a1 = DirectedGraphNode(1)
a2 = DirectedGraphNode(2)
a3 = DirectedGraphNode(3)
a4 = DirectedGraphNode(4)
a5 = DirectedGraphNode(5)

a0.neighbors += [a1, a2, a3]
a1.neighbors.append(a4)
a2.neighbors += [a4, a5]
a3.neighbors += [a4, a5]

test = []
test += [a0, a1, a2, a3, a4, a5]
result = a.topSort(test)
for i in result:
    print i.label
