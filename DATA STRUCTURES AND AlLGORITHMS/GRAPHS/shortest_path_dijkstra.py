"""
Shortest Path - Dijkstra's Algorithm

Finds the shortest distance from a source vertex to all other vertices
in a weighted graph with non-negative edge weights.
Uses a min-heap (priority queue) for efficiency.

Time Complexity  : O((V + E) log V)
Space Complexity : O(V)
"""

import heapq


def dijkstra(graph, src, v):
    dist = [float('inf')] * v
    dist[src] = 0
    min_heap = [(0, src)]  # (distance, vertex)

    while min_heap:
        curr_dist, u = heapq.heappop(min_heap)

        # skip if we already found a shorter path
        if curr_dist > dist[u]:
            continue

        for neighbor, weight in graph.get(u, []):
            new_dist = dist[u] + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(min_heap, (new_dist, neighbor))

    return dist


try:
    v = int(input("ENTER NUMBER OF VERTICES: "))
    e = int(input("ENTER NUMBER OF EDGES: "))

    if v <= 0:
        raise ValueError("Vertices must be greater than 0.")

    graph = {i: [] for i in range(v)}

    for _ in range(e):
        u, w, wt = map(int, input("ENTER EDGE (u v weight): ").split())
        if u >= v or w >= v:
            raise ValueError("Vertex index out of range.")
        graph[u].append((w, wt))
        graph[w].append((u, wt))

    src = int(input("ENTER SOURCE VERTEX: "))

    if src >= v:
        raise ValueError("Source vertex out of range.")

    distances = dijkstra(graph, src, v)

    print(f"\nSHORTEST DISTANCES FROM VERTEX {src}:")
    for i, d in enumerate(distances):
        print(f"  TO VERTEX {i}: {d if d != float('inf') else 'UNREACHABLE'}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
