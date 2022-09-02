import math

class Prim:

    def min_key(self,key,visited,v):
        min = math.inf

        for i in range(v):
            if key[i] < min and i not in visited:
                min_idx = i
                min = key[i]
        return min_idx

    def minimum_spanning_tree(self,graph):
        # Find minimum edges
        vertices = len(graph)
        key = [math.inf] * vertices
        key[0] = 0
        parent = [None]*vertices
        parent[0] = -1
        visited = set()
        for i in range(vertices):

            u = self.min_key(key,visited,vertices)

            visited.add(u)

            for v in range(vertices):
                if graph[u][v] != 0 and v not in visited and graph[u][v] < key[v]:
                    key[v] = graph[u][v]
                    parent[v] = u

        

                

            


graph = [[0, 2, 0, 6, 0],
         [2, 0, 3, 8, 5],
         [0, 3, 0, 0, 7],
         [6, 8, 0, 0, 9],
         [0, 5, 7, 9, 0]]
Prim().minimum_spanning_tree(graph)