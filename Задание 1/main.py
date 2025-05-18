def dijkstra(graph, start):
    n = len(graph)
    distances = [float('infinity')] * n
    distances[start] = 0
    visited = [False] * n
    
    while True:
        # Находим вершину с минимальным расстоянием среди непосещённых
        min_distance = float('infinity')
        current_vertex = -1
        for v in range(n):
            if not visited[v] and distances[v] < min_distance:
                min_distance = distances[v]
                current_vertex = v
        
        # Если все вершины посещены или граф несвязный
        if current_vertex == -1:
            break
        
        visited[current_vertex] = True
        
        # Обновляем расстояния до соседей
        for neighbor in range(n):
            if graph[current_vertex][neighbor] > 0:  # Если есть ребро
                new_distance = distances[current_vertex] + graph[current_vertex][neighbor]
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
    
    return distances

if __name__ == "__main__":
    # Пример графа (матрица смежностей)
    graph = [
        [0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
    ]
    
    start_vertex = 0
    distances = dijkstra(graph, start_vertex)
    
    print(f"Кратчайшие расстояния от вершины {start_vertex}:")
    for vertex, distance in enumerate(distances):
        print(f"До вершины {vertex}: {distance}")
