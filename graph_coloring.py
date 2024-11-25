class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def is_safe(self, vertex, color, final_colors):
        for i in self.graph[vertex]:
            if final_colors[i] == color:
                return False
        return True
    
    def graph_coloring_utils(self, max_colors, final_colors, current_vertex):
        if current_vertex == self.vertices:
            return True
        
        for color in range(1, max_colors+1):
            if self.is_safe(current_vertex, color, final_colors):
                final_colors[current_vertex] = color

                if self.graph_coloring_utils(max_colors, final_colors, current_vertex+1):
                    return True
                
                final_colors[current_vertex] = 0
        return False
    
    def graph_coloring(self, max_colors):
        final_colors = [0]*self.vertices

        if self.graph_coloring_utils(max_colors, final_colors, 0):
            for i in range(self.vertices):
                print(f"Station {i+1} :- Frequency {final_colors[i]}")
            return
            
        print("No solution exits!!")
        return
    
if __name__ == "__main__":
    g = Graph(5)

    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)

    m = 3
    g.graph_coloring(m)