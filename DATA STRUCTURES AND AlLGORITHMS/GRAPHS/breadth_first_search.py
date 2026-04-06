"""
Breadth First Search (BFS)

Explores all neighbors of a node before moving to the next level.
Uses a queue internally.
Useful for finding shortest path in an unweighted graph.

Time Complexity  : O(V + E)  - V = vertices, E = edges
Space Complexity : O(V)      - for the visited set and queue
"""

from collections import deque


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


try:
    v = int(input("ENTER NUMBER OF VERTICES: "))
    e = int(input("ENTER NUMBER OF EDGES: "))

    if v <= 0:
        raise ValueError("Vertices must be greater than 0.")

    graph = {}

    for _ in range(e):
        u, w = map(int, input("ENTER EDGE (u v): ").split())
        if u not in graph:
            graph[u] = []
        if w not in graph:
            graph[w] = []
        graph[u].append(w)
        graph[w].append(u)

    start = int(input("ENTER START VERTEX: "))

    if start not in graph:
        raise ValueError(f"Vertex {start} not found in graph.")

    result = bfs(graph, start)
    print(f"BFS TRAVERSAL ORDER: {result}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
