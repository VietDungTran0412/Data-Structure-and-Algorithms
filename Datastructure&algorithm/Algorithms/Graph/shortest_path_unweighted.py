class Solution:
    def print(self):
        edges = [("Hanoi","Haiphong"),("Haiphong","Hungyen"),("Haiphong","Thaibinh"),
                ("Hanoi","Hungyen"),("Thaibinh","Quangninh"),("Hungyen","Mongcai"),("Mongcai","Quangninh")]
        self.shortest_path("Hanoi","Quangninh",edges)
    def build_graph(self,edges):
        graph = {}
        for src, dest in edges:
            if src not in graph:
                graph[src] = [dest]
            elif src in graph:
                graph[src].append(dest)
            if dest not in graph:
                graph[dest] = [src]
            elif dest in graph:
                graph[dest].append(src)
        print(graph)
        return graph

    def shortest_path_util(self,pred,dist,src,dest,graph):
        visited = set()
        visited.add(src)
        q = [src]

        while len(q)>0:
            temp = q[0]
            q=q[1:]
            for edge in graph[temp]:
                if edge not in visited:
                    # dist[edge] = dist[temp]+1
                    pred[edge] = temp
                    visited.add(edge)
                    q.append(edge)
                    if edge == dest:
                        return True
        return False

    def shortest_path(self,src,dest,edges):
        graph = self.build_graph(edges)

        distances = [-1]*len(graph)
        pred = {}
        if self.shortest_path_util(pred,distances,src,dest,graph):
            path = [dest]

            crawl = dest

            while crawl in pred:
                path.append(pred[crawl])
                crawl = pred[crawl]
            print(path) 


Solution().print()