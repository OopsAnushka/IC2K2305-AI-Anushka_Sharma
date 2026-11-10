
import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('G', 4)],
    'E': [('G', 2)],
    'F': [('G', 2)],
    'G': []
}

heuristic = {
    'A': 6,
    'B': 5,
    'C': 4,
    'D': 4,
    'E': 2,
    'F': 2,
    'G': 0
}

def a_star(start, goal):
    queue = [(heuristic[start], 0, start, [start])]
    visited = {}

    while queue:
        f, cost, node, path = heapq.heappop(queue)

        if node == goal:
            print("Shortest Path:", " -> ".join(path))
            print("Total Cost:", cost)
            return

        if node in visited and visited[node] <= cost:
            continue

        visited[node] = cost

        for neighbour, edge_cost in graph[node]:
            new_cost = cost + edge_cost
            new_f = new_cost + heuristic[neighbour]

            heapq.heappush(
                queue,
                (new_f, new_cost, neighbour, path + [neighbour])
            )

print("A* Search:")
a_star('A', 'G')
