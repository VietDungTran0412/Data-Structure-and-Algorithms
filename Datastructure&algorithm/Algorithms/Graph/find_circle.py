class Solution:
    def depth_first_count(self,start,graph,visited):
        if start in visited:
            return 0
        visited.add(start)
        for i in range(len(graph[start])):
            if graph[start][i] == 1 and i not in visited:
                self.depth_first_count(i,graph,visited)
        return 1

    def count_circle(self,graph):
        visited = set()
        count = 0 
        for i in range(len(graph)):
            count += self.depth_first_count(i,graph,visited)
        return count

graph = [[1,0,0],[0,1,0],[0,0,1]]
print(Solution().count_circle(graph))