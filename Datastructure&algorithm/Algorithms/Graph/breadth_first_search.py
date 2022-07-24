from Graph import Graph
class BreadthFirstSearch:
    def getPaths(self,graph,vertex):
        print(self.bfs(graph,vertex))
    def bfs(self,graph: Graph,vertex):
        if vertex not in graph.graph_dict:
            return []
        nodes = [vertex]
        visited = set()
        q = [vertex]
        while len(q)>0:
            cur = q[0]
            q = q[1:]
            visited.add(cur)
            for edge in graph.graph_dict[cur]:
                if edge not in visited:
                    nodes.append(edge)
                    q.append(edge)
                    visited.add(edge)
        return nodes
routes = [("Hanoi","Haiphong"),("Hanoi","Thainguyen"),("Hanoi","Langson"),
            ("Haiphong","Haiduong"),("Haiduong","Halong")]
graph = Graph(routes)
BreadthFirstSearch().getPaths(graph,"Hanoi")