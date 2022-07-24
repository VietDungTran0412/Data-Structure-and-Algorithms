class Graph:
    def __init__(self,edges) -> None:
        self.edges = edges
        self.graph_dict = {}
        for start, end in edges:
            if start not in self.graph_dict:
                self.graph_dict[start] = [end]
            else:
                self.graph_dict[start].append(end)
            if end not in self.graph_dict:
                self.graph_dict[end] = [start]
            else:
                self.graph_dict[end].append(start)
        print("Graph Dict:",self.graph_dict) 






