
class Solution:
    def __repr__(self) -> str:
        graph = [[4,3,1],[3,2,4],[3],[4],[]]
        return str(self.allPathsSourceTarget(graph))
    def buildGraph(self,edges):
        graph = {}
        for i in range(len(edges)):
            graph[i] = edges[i]
        return graph
    paths = []

    def getAllPaths(self,start,end,path,result,graph):
        if start >= end:
            return
        path.append(start)
        if start == end-1:
            result.append(path.copy())

        for i in range(len(graph[start])):
            self.getAllPaths(graph[start][i],end,path,result,graph)
        path.pop()
    def allPathsSourceTarget(self,graph):
        result = []
        path = []
        n = len(graph)
        self.getAllPaths(0,n,path,result,graph)
        return result
print(Solution())