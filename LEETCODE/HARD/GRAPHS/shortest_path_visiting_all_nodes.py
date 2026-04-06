"""
You have an undirected, connected graph of n nodes labeled from 0 to n - 1. You are given an array graph where graph[i] is a list of all the nodes connected with node i by an edge.

Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.

Example 1:
Input: graph = [[1,2,3],[0],[0],[0]]
Output: 4

Example 2:
Input: graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
Output: 4

Constraints:
- n == graph.length
- 1 <= n <= 12
- 0 <= graph[i].length < n
- graph[i] does not contain i.
- If graph[a] contains b, then graph[b] contains a.
- The input graph is always connected.
"""

from collections import deque

def shortest_path_length(graph):
    n = len(graph)
    target = (1 << n) - 1
    queue = deque([(i, 1 << i, 0) for i in range(n)])
    visited = {(i, 1 << i) for i in range(n)}
    
    while queue:
        node, mask, dist = queue.popleft()
        
        if mask == target:
            return dist
        
        for neighbor in graph[node]:
            new_mask = mask | (1 << neighbor)
            if (neighbor, new_mask) not in visited:
                visited.add((neighbor, new_mask))
                queue.append((neighbor, new_mask, dist + 1))
    
    return -1

try:
    n = int(input("ENTER N\n"))
    graph = []
    print("ENTER GRAPH (neighbors space separated):")
    for _ in range(n):
        neighbors = list(map(int, input().split()))
        graph.append(neighbors)
    print(f"SHORTEST PATH: {shortest_path_length(graph)}")
except Exception as e:
    print(f"An error occurred: {e}")
