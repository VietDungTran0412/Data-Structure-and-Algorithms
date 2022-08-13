class BreadthFirstSearch:
    def __init__(self,edges) -> None:
        self.graph_dict = {}
        for start,end in edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            elif start not in self.graph_dict:
                self.graph_dict[start] = [end]
            if end in self.graph_dict:
                self.graph_dict[end].append(start)
            elif end not in self.graph_dict:
                self.graph_dict[end] = [start]
        print(self.graph_dict)
    def search(self,start):
        if start not in self.graph_dict:
            return []
        q = [start]
        visited = set()
        visited.add(start)
        path = [start]
        while len(q)>0:
            temp = q[0]
            q = q[1:]
            if temp in self.graph_dict:
                for edge in self.graph_dict[temp]:
                    if edge not in visited:
                        visited.add(edge)
                        path.append(edge)
                        q.append(edge)
        return path
bfs = BreadthFirstSearch([("Hanoi","Haiphong"),("Hanoi","Thainguyen"),("Hanoi","Langson"),
            ("Haiphong","Haiduong"),("Haiduong","Halong")])
print(bfs.search("Hanoi"))