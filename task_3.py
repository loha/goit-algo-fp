import heapq

def dijkstra(graph, start):
    # Ініціалізація
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))
    shortest_paths = {vertex: float('inf') for vertex in graph}
    shortest_paths[start] = 0
    visited = set()

    while priority_queue:
        (current_distance, current_vertex) = heapq.heappop(priority_queue)
        
        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_paths

# Створення графу
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Виклик алгоритму Дейкстри для вершини 'A'
shortest_paths = dijkstra(graph, 'A')

# Виведення результатів
print("Найкоротші шляхи від вершини 'A':")
for vertex, distance in shortest_paths.items():
    print(f"Від 'A' до '{vertex}' відстань {distance}")
