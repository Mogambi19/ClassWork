import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # If undirected, remove if directed

    def display(self):
        for node in self.graph:
            print(f"{node} --> {self.graph[node]}")

    def dijkstra(self, start):
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        visited = set()
        pq = [(0, start)]

        while pq:
            current_distance, current_node = heapq.heappop(pq)

            if current_node in visited:
                continue
            visited.add(current_node)

            for neighbor, weight in self.graph[current_node]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        return distances

    def shortest_path_first(self, start):
        # This is essentially the same as Dijkstra’s, labeled differently
        return self.dijkstra(start)


# Example usage
if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B', 4)
    g.add_edge('A', 'C', 2)
    g.add_edge('B', 'C', 5)
    g.add_edge('B', 'D', 10)
    g.add_edge('C', 'E', 3)
    g.add_edge('E', 'D', 4)
    g.add_edge('D', 'F', 11)

    print("Graph:")
    g.display()

    print("\nDijkstra’s Shortest Paths from A:")
    distances = g.dijkstra('A')
    for node in distances:
        print(f"Distance to {node}: {distances[node]}")

    print("\nShortest Path First (Same as Dijkstra) from A:")
    spf = g.shortest_path_first('A')
    for node in spf:
        print(f"Distance to {node}: {spf[node]}")