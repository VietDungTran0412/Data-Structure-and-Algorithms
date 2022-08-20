class Solution:
    def __repr__(self) -> str:
        return str(self.findSmallestSetOfVertices(5,[[0,1],[2,1],[3,1],[1,4],[2,4]]))
    def buildGraph(self,edges):
        graph = {}
        for start, end in edges:
            if start not in graph:
                graph[start] = [end]
            else:
                graph[start].append(end)
        return graph
    def findSmallestSetOfVertices(self,n: int, edges: list[list[int]])->list[int]:
        vertices = set([i for i in range(n)])
        graph = self.buildGraph(edges)
        for v in graph:
            for edge in graph[v]:
                if edge in vertices:
                    vertices.remove(edge)
        res = []
        for i in vertices:
            res.append(i)
        return res
print(Solution())