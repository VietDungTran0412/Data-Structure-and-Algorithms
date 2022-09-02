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
class AdjGraph:
    def __init__(self,adj_matrix) -> None:
        self.graph = {}
        for i in range(len(adj_matrix)):
            self.graph[i] = []
            for j in range(len(adj_matrix[i])):
                if adj_matrix[i][j] == 1:
                    self.graph[i].append(j)
        print(self.graph)
class AdjNode:
    def __init__(self,val) -> None:
        self.vertex = val
        self.next = None
class GraphAlter:
    def __init__(self,vertices) -> None:
        self.V = vertices
        self.graph = [None]*self.V
    def add_edge(self,source,destination):
        node = AdjNode(destination)
        node.next = self.graph[source]
        self.graph[source] = node

        node = AdjNode(source)
        node.next = self.graph[destination]
        self.graph[destination] = node
    def print_graph(self):
        for i in range(self.V):
            cur = self.graph[i]
            while cur:
                print(cur.vertex,end="->")
                cur = cur.next
            print()
class GraphNode:
    def __init__(self,val,neighbors = None) -> None:
        self.val = val
        self.neighbors = neighbors if neighbors else []

class GraphList:
    def __init__(self,vertices) -> None:
        self.V = vertices
        self.graph = [None]*self.V
    def add_edge(self,src,dest):
        if self.graph[src] is None:
            self.graph[src] = GraphNode(src,[dest])
        elif self.graph[src] is not None:
            self.graph[src].neighbors.append(dest)
        if self.graph[dest] is None:
            self.graph[dest] = GraphNode(dest,[src])
        elif self.graph[dest] is not None:
            self.graph[dest].neighbors.append(src)
    def print(self):
        for i in range(self.V):
            print(self.graph[i].neighbors)

def main():
    graph = GraphList(5)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.print()

main()

