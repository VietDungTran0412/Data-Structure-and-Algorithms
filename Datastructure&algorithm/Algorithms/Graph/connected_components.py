class Solution:
    def search_connection(self,start,graph,visited):
        path = []
        if start in visited:
            return []
        visited.add(start)
        path.append(start)
        if start in graph:
            for v in graph[start]:
                path += self.search_connection(v,graph,visited)
        
        return path
                
    def connected_components(self,graph):
        components = []
        visited = set()
        for v in graph:
            if v not in visited:
                component = self.search_connection(v,graph,visited)
                components.append(component)
        return components
graph = {0:[1],
        1:[0,2],
        2:[1],
        3:[4],
        4:[3]
    }
print(Solution().connected_components(graph))