class Solution:
    def build_graph(self,connections):
        graph = {}
        for start, end in connections:
            if start not in connections:
                graph[start] = [end]
            else:
                graph[start].append(end)
        return graph
    def count_negative_routes(self,graph,visited,start):
        visited.add(start)
        if start in graph:
            for v in graph[start]:
                if v not in visited:
                    self.count_negative_routes(graph,visited,v)



    def reorder_routes(self,connections,n):
        graph = self.build_graph(connections)
        visited = set()
        count = 0
        self.count_negative_routes(graph,visited,0)
        if len(visited) == n -1:
            count += len(visited)
        for v in graph:
            if v not in visited:
                for e in graph[v]:
                    if e not in visited:
                        count += 1

        