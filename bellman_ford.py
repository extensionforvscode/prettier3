class Graph:
    def __init__(self, v):
        self.vertices = v
        self.graph = []

    def add_edges(self, u, v, cost):
        self.graph.append([u, v, cost])

    def bellman_ford(self, start):
        final_distances = [100]*(self.vertices-1)
        final_distances[start] = 0

        for _ in range(self.vertices - 1):
            for u,v,cost in self.graph:
                if final_distances[u] != 100 and final_distances[u] + cost < final_distances[v]:
                    final_distances[v] = final_distances[u] + cost
        
        for u,v,cost in self.graph:
            if final_distances[u] != 100 and final_distances[u] + cost < final_distances[v]:
                print("Negative Weight Cycle Detected !!!")
                print("<NO SOLUTION>")
                return
        
        print("Here's the final solution :- ")
        for i in range(self.vertices-1):
            print(f"Vertex {i} : {final_distances[i]}")
        return
    
if __name__ == "__main__":
    graph = Graph(5)

    graph.add_edges(0, 1, 4)
    graph.add_edges(0, 3, 5)
    graph.add_edges(3, 2, 3)
    graph.add_edges(2, 1, -10)
    graph.add_edges(1, 3, 5)

    graph.bellman_ford(0)
