from Graph import Graph
class Solution:
    def __repr__(self) -> str:
        graph = self.build_graph()
        sp = self.getShortestPath(graph,"Hanoi","Halong")
        return str(sp)
    def build_graph(self):
        routes = [("Hanoi","Haiphong"),("Hanoi","Hungyen"),("Hanoi","Thanhhoa"),
        ("Haiphong","Halong"),("Hungyen","Haiphong"),("Thanhhoa","Hungyen"),]
        return Graph(routes)
    def getShortestPath(self,graph: Graph, start: str, end: str):
        
        if start == end:
            return ["Same node"]
        if start not in graph.graph_dict:
            return None
        q = graph.graph_dict[start]
        distance = {}
        shortest = 1000
        while len(q)>0:
            temp = q[0]

            

print(Solution())