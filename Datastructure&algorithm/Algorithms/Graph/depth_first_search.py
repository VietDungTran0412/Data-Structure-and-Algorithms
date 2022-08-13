from Graph import Graph
class DepthFirstSearch:
    def __init__(self,edges) -> None:
        self.graph_dict = {}
        for start,end in edges:
            if start not in self.graph_dict:
                self.graph_dict[start] = [end]
            elif start in self.graph_dict:
                self.graph_dict[start].append(end)
            if end not in self.graph_dict:
                self.graph_dict[end] = [start]
            elif end in self.graph_dict:
                self.graph_dict[end].append(start)
        print(self.graph_dict)
    def search(self,start,visited = set()):
        if start in visited:
            return []
        if start not in self.graph_dict:
            return []
        visited.add(start)
        path = [start]
        if start in self.graph_dict:
            for edge in self.graph_dict[start]:
                if edge not in visited:
                    path += self.search(edge,visited)
                    visited.add(edge)
        return path

edges = routes = [("Hanoi","Haiphong"),("Hanoi","Thainguyen"),("Hanoi","Langson"),
            ("Haiphong","Haiduong"),("Haiduong","Halong")]
dfs = DepthFirstSearch(edges)
print(dfs.search("Hanoi"))