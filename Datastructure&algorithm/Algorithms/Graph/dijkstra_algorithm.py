
import math
class MinHeap:
    def __init__(self,maxsize) -> None:
        self.ar = [None]*maxsize
        self.size = 0
        self.capacity = maxsize
    def parent(self,pos):
        return (pos-1)//2
    def left_child(self,pos):
        left = 2*pos +1
        if left >= self.size:
            return -1
        return left
    def right_child(self,pos):
        right =2*pos+2
        if right >= self.size:
            return -1
        return right
    def percolate_down(self,pos):
        if self.left_child(pos) != -1 and self.ar[pos]['cost'] >= self.ar[self.left_child(pos)]['cost']:
            min = self.left_child(pos)
        else:
            min = pos
        if self.right_child(pos) != -1 and self.ar[min]['cost'] >= self.ar[self.right_child(pos)]['cost']:
            min = self.right_child(pos)
        if min != pos:
            self.ar[pos], self.ar[min] = self.ar[min], self.ar[pos]
            self.percolate_down(min)
    def delete(self):
        if self.size == 0:
            return -1
        temp = self.ar[0]
        last = self.size - 1
        self.ar[0], self.ar[last] = self.ar[last],self.ar[0]
        self.ar[last] = None
        self.size -= 1
        self.percolate_down(0)
        return temp
    def insert(self,val):
        if self.size == self.capacity:
            return
        self.ar[self.size] = val
        i = self.size
        self.size += 1
        self.percolate_up(i)
    def percolate_up(self,i):
        while i != 0:
            parent = self.parent(i)
            if self.ar[parent]['cost'] > self.ar[i]['cost']:
                self.ar[i], self.ar[parent] = self.ar[parent], self.ar[i]
                i = parent
            else:
                break

class Dijkstra:
    def add_edges_cost(self,start,graph,table,visited):
        if start not in visited:
            table[start] = {'key':start,'cost':math.inf,'pred':None}
            visited.add(start)
        if start in graph:
            for v in graph[start]:
                if v not in visited:
                    self.add_edges_cost(v,graph,table,visited)

    def shortest_path(self,graph,src,dest):
        table = {}
        visited = set()
        self.add_edges_cost(src,graph,table,visited)
        table[src] = {'key': src, 'cost':0,'pred':None}
        min_heap = MinHeap(len(table))
        min_heap.insert(table[src])
        while min_heap.size != 0:
            temp = min_heap.delete()
            if temp['key'] in graph:
                for v in graph[temp['key']]:
                    distance = graph[temp['key']][v] + table[temp['key']]['cost']
                    if distance < table[v]['cost']:
                        table[v]['cost'] = distance
                        table[v]['pred'] = temp['key']
                        min_heap.insert(table[v])
        path = [dest]
        crawl = dest
        while crawl != src:
            path.append(table[crawl]['pred'])
            crawl = table[crawl]['pred']
        return path[::-1]
    def min_key(self,key,visited,v):
        min = math.inf
        for i in range(v):
            if key[i] < min and i not in visited:
                min_idx = i
        return min_idx
    def shortest_path_alter(self,graph,start,end):
        vertices = len(graph)
        key = [math.inf]* vertices
        visited = set()
        parent = [None]*vertices
        parent[start] = -1
        key[start] = 0
        is_finding = False
        for i in range(vertices):

            u = self.min_key(key,visited,vertices)
            visited.add(u)
            if u == end:
                is_finding = True
                break
            
            for v in range(vertices):
                distance = key[u] + graph[u][v]
                if graph[u][v] != 0 and v not in visited and distance < key[v]:
                    key[v] = distance
                    parent[v] = u
        if is_finding:
            path = [end]
            crawl = end
            while parent[crawl] != -1:
                path.append(parent[crawl])
                crawl = parent[crawl]
            return path[::-1]





# graph = {
#     1:{2:2,3:5,4:2},
#     2:{1:2,3:3,5:1},
#     3:{1:5,4:3,2:3,5:1,8:1,6:1},
#     4:{1:2,3:3,7:2},
#     5:{2:1,9:7,3:1},
#     6:{3:1,8:3,7:2},
#     7:{4:2,6:2},
#     8:{3:1,6:3,9:1},
#     9:{5:7,8:1}
# }
graph = [[0,6,0,1,0],
         [6,0,5,2,2],
         [0,5,0,0,5],
         [1,2,0,0,1],
         [0,2,5,1,0]]
print(Dijkstra().shortest_path_alter(graph,0,2)) # Directed graph