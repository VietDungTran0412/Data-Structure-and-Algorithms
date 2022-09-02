class Solution:
    def print_solution(self):
        graph = [[],[],[3],[1],[0,1],[2,0]]
        self.topological_sort(graph)
    def topological_sort_util(self,v,visited,stack,graph):
        if v not in visited:
            visited.add(v)
        for i in range(len(graph[v])):
            if graph[v][i] not in visited:
                self.topological_sort_util(graph[v][i],visited,stack,graph)
        stack.append(v)
        
    def topological_sort(self,graph):
        visited = set()
        stack =[]

        for i in range(len(graph)):
            if i not in visited:
                self.topological_sort_util(i,visited,stack,graph)
        print(stack[::-1])
Solution().print_solution()