import math
class BellmannFord:
    def add_edges(self,start,table,graph,visited):
        if start not in visited:
            visited.add(start)
            table[start] = {'cost':math.inf,'pred':None}
        if start in graph:
            for v in graph[start]:
                self.add_edges(v,table,graph,visited)

    def single_shortest_path(self,graph,start,end):
        table = {}
        self.add_edges(start,table,graph,visited=set())
        table[start] = {'cost':0,'pred':None}
        process = len(table)-1
        for i in range(process):
            for v in graph:
                for neighbor in graph[v]:
                    distance = table[v]['cost'] + graph[v][neighbor]
                    if distance < table[neighbor]['cost']:
                        table[neighbor]['cost'] = distance
                        table[neighbor]['pred'] = v
        crawl = end
        path = [end]
        print(table)
        while crawl != start:
            path.append(table[crawl]['pred'])
            crawl = table[crawl]['pred']
        return path[::-1]

                

graph = {
    1:{2:4,4:5},
    2:{},
    3:{2:-10},
    4:{3:3}
}

    # 1:{2:6,3:5,4:5},
    # 2:{5:-1},
    # 3:{2:-2},
    # 4:{3:-2,6:-1},
    # 5:{7:3},
    # 6:{7:3},

print(BellmannFord().single_shortest_path(graph,1,4))