"""
Depth First Search (DFS)

Explores as far as possible along each branch before backtracking.
Can be implemented iteratively (stack) or recursively.
Useful for cycle detection, topological sort, and connected components.

Time Complexity  : O(V + E)
Space Complexity : O(V)  - for visited set and call stack
"""


def dfs_recursive(graph, node, visited, order):
    visited.add(node)
    order.append(node)

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, order)


def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    order = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            order.append(node)
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)

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

    choice = input("USE RECURSIVE OR ITERATIVE? (r/i): ").strip().lower()

    if choice == 'r':
        visited = set()
        order = []
        dfs_recursive(graph, start, visited, order)
        print(f"DFS TRAVERSAL ORDER (RECURSIVE): {order}")
    else:
        result = dfs_iterative(graph, start)
        print(f"DFS TRAVERSAL ORDER (ITERATIVE): {result}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
