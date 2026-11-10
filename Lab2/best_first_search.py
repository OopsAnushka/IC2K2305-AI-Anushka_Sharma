
import heapq

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 3,
    'E': 2,
    'F': 1,
    'G': 0
}

def best_first_search(start, goal):
    priority_queue = [(heuristic[start], start)]
    visited = set()

    while priority_queue:
        _, node = heapq.heappop(priority_queue)

        if node in visited:
            continue

        print(node, end=" ")
        visited.add(node)

        if node == goal:
            return

        for neighbour in graph[node]:
            if neighbour not in visited:
                heapq.heappush(
                    priority_queue,
                    (heuristic[neighbour], neighbour)
                )

print("Best First Search Traversal:")
best_first_search('A', 'G')
