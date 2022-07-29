class Solution:
    def getAllPaths(self,graph_dict,start,end):
        if start == end:
            return [start]
        res = [start]
        for node in graph_dict[start]:
            res += self.getAllPaths(graph_dict,node,end)
        return res

    def allPathsSourceTarget(self,graph):
        graph_dict = {}
        for i in range(len(graph)):
            graph_dict[i] = graph[i]
        des = len(graph_dict)-1
        res = []
        for node in graph_dict[0]:
            res += self.getAllPaths(0,des)