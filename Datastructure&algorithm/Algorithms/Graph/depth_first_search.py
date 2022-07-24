from Graph import Graph
class DepthFirstSearch:
    def getPaths(self,graph: Graph,vertex):
        print(self.dfs(graph,vertex))
    def dfs(self,graph: Graph,vertex,visited = set()):
        paths = [vertex]
        visited.add(vertex)
        # if vertex not in graph.graph_dict:
        #     return paths
        for neighbor in graph.graph_dict[vertex]:
            if neighbor not in visited:
                paths += self.dfs(graph,neighbor,visited)
        return paths
routes = [("Hanoi","Haiphong"),("Haiphong","Hungyen"),("Hanoi","Hungyen"),("Haiphong","Thainguyen"),("Thainguyen","Hungyen")]
graph = Graph(routes)
DepthFirstSearch().getPaths(graph,"Hanoi")