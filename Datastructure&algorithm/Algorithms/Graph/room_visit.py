class Solution:
    def __repr__(self) -> str:
        rooms = [[1,3],[3,0,1],[2],[0]]
        return str(self.canVisitAllRooms(rooms))
    def buildGraph(self,edges: list[list[int]]):
        graph = {}
        for i in range(len(edges)):
            graph[i] = edges[i]
        return graph
    def visitAllRooms(self,graph,start,visited,length):
        if start in visited:
            return
        visited.add(start)
        for edge in graph[start]:
            if edge not in visited:
                self.visitAllRooms(graph,edge,visited,length)

    def canVisitAllRooms(self,rooms: list[list[int]]):
        graph = self.buildGraph(rooms)
        visited = set()
        self.visitAllRooms(graph,0,visited,len(rooms))
        print(visited)
        return len(visited) == len(rooms)
print(Solution())
class GraphNode:
    def __init__(self,val,neighbors = None) -> None:
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
